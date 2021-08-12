using System;
using System.IO;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Extensions.Http;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Logging;
using Newtonsoft.Json;
using System.Collections.Generic;
using AzureFunctions_NET.Models;
using System.Linq;

namespace AzureFunctions_NET
{
    public static class GetLatest
    {
        [FunctionName("GetLatest")]
        public static async Task<IActionResult> Run(
            [HttpTrigger(AuthorizationLevel.Function, "get", Route = null)] HttpRequest req,
            [CosmosDB(databaseName: "IOT", collectionName: "Messages", CreateIfNotExists = true, ConnectionStringSetting = "CosmosDB", SqlQuery = "SELECT TOP 1 * FROM c ORDER BY c._ts DESC")] IEnumerable<DhtData> cosmos,
            ILogger log)
        {

            return new OkObjectResult(cosmos.FirstOrDefault());
        }
    }
}
