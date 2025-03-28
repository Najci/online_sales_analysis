from product import Product
from product_manager import ProductManager

# Initialize ProductManager
manager = ProductManager()

# Add some products
manager.add_product(Product("PC", 1200, 5))
manager.add_product(Product("Mouse", 800, 10))
manager.add_product(Product("Earbuds", 150, 15))
