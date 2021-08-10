#pip install azure-iot-device
#PS     $env:IOTDEVICE_CONNECTIONSTRING='enter_the_connectionstring_here'
#CMD    set IOTDEVICE_CONNECTIONSTRING=enter_the_connectionstring_here
#Bash   export IOTDEVICE_CONNECTIONSTRING="enter_the_connectionstring_here"
#os.getenv("IOTDEVICE_CONNECTIONSTRING")

import os
import json
import asyncio
from azure.iot.device.aio import IoTHubDeviceClient

async def main():
    IOTDEVICE_CONNECTIONSTRING = "HostName=pyt21-iothub.azure-devices.net;DeviceId=python-device;SharedAccessKey=k+MNG688h+2jMpKILRu3xlzCZN4GIFVGDhndAwKidk0="
    device_client = IoTHubDeviceClient.create_from_connection_string(IOTDEVICE_CONNECTIONSTRING)
    await device_client.connect()

    #sending message
    while True:
        await device_client.send_message(json.dumps({"message":"this is a message"}))
        print('Message was sent!')
        await asyncio.sleep(10)


if __name__ == '__main__':
    asyncio.run(main())