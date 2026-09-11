orders = []

def create_order(username, items):
    order = {"username": username, "items": items, "status": "Placed"}
    orders.append(order)
    return order

def get_orders(username):
    return [o for o in orders if o["username"] == username]
