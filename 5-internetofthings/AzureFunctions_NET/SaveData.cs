using IoTHubTrigger = Microsoft.Azure.WebJobs.EventHubTriggerAttribute;

using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Host;
using Microsoft.Azure.EventHubs;
using System.Text;
using System.Net.Http;
using Microsoft.Extensions.Logging;

namespace AzureFunctions_NET
{
    public static class SaveData
    {
        private static HttpClient client = new HttpClient();

        [FunctionName("SaveData")]
        public static void Run(
            [IoTHubTrigger("messages/events", Connection = "IotHubEndpoint")]EventData message, 
            [CosmosDB(databaseName:"IOT", collectionName: "Messages", CreateIfNotExists = true, ConnectionStringSetting = "CosmosDB")] out dynamic cosmos,
            ILogger log)
        {
            try
            {
                cosmos = Encoding.UTF8.GetString(message.Body.Array);
            }
            catch
            {
                cosmos = null;
            }
            

        }
    }
}