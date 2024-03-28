using Microsoft.AspNetCore.Mvc;

namespace SmartCityExample.Controllers
{
    public class ProductTypeController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }
    }
}