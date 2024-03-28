using System;

namespace SmartCityExample.Models
{
    public class Product 
    {
        public int ProductId { get; set; }
        public required String ProductName { get; set; }
        public required String Characteristics { get; set; }
        public double AveragePrice { get; set; }
        public required String Logo { get; set; }
        public bool Active { get; set; }

        // Product Type Reference
        public required ProductType Type { get; set; }
    }
}