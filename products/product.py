products = []

def add_product(name, price):
    product = {
        "name": name,
        "price": price
    }

    products.append(product)
    return "Product added successfully"

def list_products():
    return products