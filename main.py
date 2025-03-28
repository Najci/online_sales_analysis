from product import Product
from product_manager import ProductManager

# Initialize ProductManager
manager = ProductManager()

# Add some products
manager.add_product(Product("Laptop", 1200, 5))
manager.add_product(Product("Phone", 800, 10))
manager.add_product(Product("Headphones", 150, 15))

# Display products and total value
manager.display_products()
print(f"Total Inventory Value: {manager.total_inventory_value()}")
