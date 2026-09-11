def search_products(products, keyword):
    return [p for p in products if keyword.lower() in p["name"].lower()]
