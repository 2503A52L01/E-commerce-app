from users.auth import register, login
from products.product import add_product, list_products
from search.search import search_products
from cart.cart import Cart
from orders.order import create_order
from payment.payment import process_payment


def application_message():
    return "Welcome to our E-Commerce Store - Online Shopping Application"


print(application_message())

print("\n--- USER AUTHENTICATION ---")
print(register("rama", "1234"))
print(login("rama", "1234"))

print("\n--- PRODUCTS ---")
add_product("Laptop", 50000)
add_product("Mouse", 1000)
print(list_products())

print("\n--- SEARCH ---")
print(search_products(list_products(), "Laptop"))

print("\n--- SHOPPING CART ---")
cart = Cart()
cart.add_item(list_products()[0])
cart.add_item(list_products()[1])
print("Cart total:", cart.total())

print("\n--- ORDER ---")
order = create_order("rama", cart.items)
print("Order:", order)

print("\n--- PAYMENT ---")
print(process_payment(cart.total()))

print("\nE-Commerce Application completed successfully.")