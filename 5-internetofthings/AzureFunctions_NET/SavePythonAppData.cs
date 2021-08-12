using IoTHubTrigger = Microsoft.Azure.WebJobs.EventHubTriggerAttribute;

using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Host;
using Microsoft.Azure.EventHubs;
using System.Text;
using System.Net.Http;
using Microsoft.Extensions.Logging;
using Newtonsoft.Json;
using AzureFunctions_NET.Models;

namespace AzureFunctions_NET
{
    public static class SavePythonAppData
    {
        private static HttpClient client = new HttpClient();

        [FunctionName("SavePythonAppData")]
        public static void Run([IoTHubTrigger("messages/events", Connection = "IotHubEndpointPython")]EventData message,
            [CosmosDB(databaseName: "IOT", collectionName: "PythonMessages", CreateIfNotExists = true, ConnectionStringSetting = "CosmosDB")] out dynamic cosmos, 
            ILogger log)
        {
            try
            {
                var data = JsonConvert.DeserializeObject<DhtData>(Encoding.UTF8.GetString(message.Body.Array));
                data.DeviceId = message.SystemProperties["iothub-connection-device-id"].ToString();         
                cosmos = JsonConvert.SerializeObject(data);
            }
            catch
            {
                cosmos = null;
            }
        }
    }
}