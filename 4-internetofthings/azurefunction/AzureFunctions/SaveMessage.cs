using IoTHubTrigger = Microsoft.Azure.WebJobs.EventHubTriggerAttribute;

using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Host;
using Microsoft.Azure.EventHubs;
using System.Text;
using System.Net.Http;
using Microsoft.Extensions.Logging;

namespace AzureFunctions
{
    public static class SaveMessage
    {
        private static HttpClient client = new HttpClient();

        [FunctionName("SaveMessage")]
        public static void Run(
            [IoTHubTrigger("messages/events", Connection = "IotHubEndpoint", ConsumerGroup = "python")]EventData message, 
            [CosmosDB(databaseName: "PythonDb", collectionName: "messages", CreateIfNotExists = true, ConnectionStringSetting = "CosmosDB")]out dynamic cosmos,
            ILogger log)
        {
            cosmos = Encoding.UTF8.GetString(message.Body.Array);
            log.LogInformation($"message: {Encoding.UTF8.GetString(message.Body.Array)}");
        }
    }
}