using System;
using System.IO;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Extensions.Http;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Logging;
using Newtonsoft.Json;

namespace AzureFunctions
{
    public static class Post
    {
        [FunctionName("Post")]
        public static IActionResult Run(
            [HttpTrigger(AuthorizationLevel.Anonymous, "post", Route = null)] HttpRequest req,
            [CosmosDB(
                databaseName: "DotNetProductCatalog",
                collectionName: "Products",
                CreateIfNotExists = true,
                ConnectionStringSetting = "CosmosDB"
            )] out dynamic cosmos,
            ILogger log)
        {
            cosmos = JsonConvert.DeserializeObject<dynamic>(new StreamReader(req.Body).ReadToEnd());
            return new OkResult();
        }
    }
}
