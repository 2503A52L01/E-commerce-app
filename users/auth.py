users = {}

def register(username, password):
    if username in users:
        return "User already exists"

    users[username] = password
    return "Registration successful"


def login(username, password):
    if username in users and users[username] == password:
        return "Login successful"

    return "Invalid username or password"