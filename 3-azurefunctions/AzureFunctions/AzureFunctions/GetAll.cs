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

namespace AzureFunctions
{
    public static class GetAll
    {
        [FunctionName("GetAll")]
        public static async Task<IActionResult> Run(
            [HttpTrigger(AuthorizationLevel.Function, "get", Route = null)] HttpRequest req,
            [CosmosDB(
                databaseName: "DotNetProductCatalog",
                collectionName: "Products",
                CreateIfNotExists = true,
                ConnectionStringSetting = "CosmosDB",
                SqlQuery = "SELECT * FROM c"
            )] IEnumerable<dynamic> cosmos,
            ILogger log)
        {
            return new OkObjectResult(cosmos);
        }
    }
}
