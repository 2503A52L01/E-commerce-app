def search_products(products, keyword):
    result = []

    for product in products:
        if keyword.lower() in product["name"].lower():
            result.append(product)

    return result