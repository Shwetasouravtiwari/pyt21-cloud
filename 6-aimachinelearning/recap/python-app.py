import asyncio
import json
from azure.iot.device.aio import IoTHubDeviceClient

async def send_data(device_client, payload):
    await device_client.send_message(json.dumps(payload))
    print('message sent: ' + json.dumps(payload))

async def main():
    device_client = IoTHubDeviceClient.create_from_connection_string("HostName=pyt21-iothub.azure-devices.net;DeviceId=pythonapp;SharedAccessKey=e2Xd3i88/2Y+5eOoiG/1+dzLbOCxDQ3YOHeMf3J/BGI=")
    device_client.connect()
    counter = 1

    while True:
        while counter < 20:
            await send_data(device_client, {'temp': 22, 'hum': 44})
            await asyncio.sleep(2)
            counter += 1

        await send_data(device_client, {'temp': 0, 'hum': 0})
        await asyncio.sleep(2)
        counter = 1

if __name__ == '__main__':
    asyncio.run(main())
