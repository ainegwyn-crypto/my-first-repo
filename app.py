def greet(name):
    if name is None:
        name = "Anonymous"
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("World"))