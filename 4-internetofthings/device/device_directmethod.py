#pip install azure-iot-device
#PS     $env:IOTDEVICE_CONNECTIONSTRING='enter_the_connectionstring_here'
#CMD    set IOTDEVICE_CONNECTIONSTRING=enter_the_connectionstring_here
#Bash   export IOTDEVICE_CONNECTIONSTRING="enter_the_connectionstring_here"
#os.getenv("IOTDEVICE_CONNECTIONSTRING")

import os
import time
import threading
from azure.iot.device import IoTHubDeviceClient, MethodResponse

def reboot_listener(device_client):
    while True:
        method_request = device_client.receive_method_request("reboot")

        print("rebooting device")
        time.sleep(20)
        print("reboot completed")

        #response
        resp_status = 200
        resp_payload = { "message": "rebooted successfully" }
        method_response = MethodResponse(method_request.request_id, resp_status, resp_payload)
        device_client.send_method_response(method_response)



def main():
    try:
        IOTDEVICE_CONNECTIONSTRING = "HostName=pyt21-iothub.azure-devices.net;DeviceId=python-device;SharedAccessKey=k+MNG688h+2jMpKILRu3xlzCZN4GIFVGDhndAwKidk0="
        device_client = IoTHubDeviceClient.create_from_connection_string(IOTDEVICE_CONNECTIONSTRING)
        device_client.connect()

        reboot_listener_thread = threading.Thread(target=reboot_listener, args=(device_client,))
        reboot_listener_thread.daemon = True
        reboot_listener_thread.start()

        while True:
            time.sleep(60)

    except KeyboardInterrupt:
        print("stopped")

if __name__ == '__main__':
    main()