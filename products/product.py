products = []

def add_product(name, price):
    products.append({"name": name, "price": price})
    return "Product added successfully"

def list_products():
    return products
