from product import Product
from product_manager import ProductManager
from cart import Cart

# Initialize ProductManager
manager = ProductManager()
cart = Cart()

# Add some products
manager.add_product(Product("Laptop", 1200, 5))
manager.add_product(Product("Phone", 800, 10))
manager.add_product(Product("Headphones", 150, 15))

# Add random products to the cart
cart.add_to_cart(manager.products[0])
cart.add_to_cart(manager.products[1])
cart.add_to_cart(manager.products[2])

# Display products and total value
manager.display_products()
print(f"Total Inventory Value: {manager.total_inventory_value()}")

# Display cart
cart.display_cart()
print(f"Total Cart Value: {cart.total_cart_value()}")
