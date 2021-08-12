import threading
import time
import requests
import asyncio
import json
from azure.iot.device import IoTHubDeviceClient, MethodResponse

def get_data():
    res = requests.get('https://pyt21-paf.azurewebsites.net/api/GetLatest?code=MUeidaATPs1wJDmVgsbN4Ur75fDZuGLCZGIgWNlaXGYlw3HUiNug2A==')
    return res.json()

def send_data(client, payload):
    client.send_message(json.dumps(payload))
    print('payload has been sent to azure iothub')

def update_reported_twin(client, payload):
    client.patch_twin_reported_properties(payload)
    print('updated device twin reported properties')

def get_desired_twin_interval(client):
    global interval
    patch = client.receive_twin_desired_properties_patch() #blocking code
    interval = patch['interval']
    print("setting the desired interval to " + str(interval) + " seconds.")

def get_interval(client):
    global cancelled
    
    while(not cancelled):
        get_desired_twin_interval(client)
        time.sleep(1)

def device_start(client):
    global cancelled
    global allow_sending

    while (not cancelled):
        method_request = client.receive_method_request("start")
        allow_sending = True

        method_response = MethodResponse(method_request.request_id, 200, {"message": "the device was started."})
        client.send_method_response(method_response)
        update_reported_twin(client, { 'sending': True })
        print('started sending messages to azure iothub')

def device_stop(client):
    global cancelled
    global allow_sending

    while (not cancelled):
        method_request = client.receive_method_request("stop")
        allow_sending = False

        method_response = MethodResponse(method_request.request_id, 200, {"message": "the device was stopped."})
        client.send_method_response(method_response)
        update_reported_twin(client, { 'sending': False })
        print('stopped sending messages to azure iothub')




async def main():
    global cancelled
    global allow_sending
    global interval
    cancelled = False
    allow_sending = True
    interval = 10

    conn_str = "HostName=pyt21-iothub-python.azure-devices.net;DeviceId=pythonapp;SharedAccessKey=DGOYNJlhZPicyG3GQpNxIrY/E2jSBnoyVf0LOnTyjCE="
    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)
    device_client.connect()

    thread_interval = threading.Thread(target=get_interval, args=(device_client,))
    thread_interval.start()

    thread_device_start = threading.Thread(target=device_start, args=(device_client,))
    thread_device_start.start()

    thread_device_stop = threading.Thread(target=device_stop, args=(device_client,))
    thread_device_stop.start()

    update_reported_twin(device_client, { 'sending': allow_sending })

    while (not cancelled):
        if allow_sending:
            data = get_data()
            send_data(device_client, data)
            update_reported_twin(device_client, data)
            time.sleep(interval)

if __name__ == '__main__':
    asyncio.run(main())