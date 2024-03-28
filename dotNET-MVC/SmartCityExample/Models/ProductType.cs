using System;

namespace SmartCityExample.Models
{
    public class ProductType 
    {
        public int TypeId { get; set; }
        public required String TypeDescription { get; set; }
        public bool Sold { get; set; }
    }
}