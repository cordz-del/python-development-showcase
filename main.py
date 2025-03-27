def greet(name):
    """Return a greeting for the given name."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name))
