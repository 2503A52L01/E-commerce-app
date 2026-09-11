orders = []

def create_order(username, items):
    order = {
        "username": username,
        "items": items,
        "status": "Placed"
    }

    orders.append(order)
    return order

def get_orders(username):
    return [
        order for order in orders
        if order["username"] == username
    ]@ order history supported
