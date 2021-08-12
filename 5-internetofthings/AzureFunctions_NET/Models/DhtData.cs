using System;
using System.Collections.Generic;
using System.Text;

namespace AzureFunctions_NET.Models
{
    public class DhtData
    {
        public string DeviceId { get; set; }
        public decimal Temperature { get; set; }
        public decimal Humidity { get; set; }
    }
}
