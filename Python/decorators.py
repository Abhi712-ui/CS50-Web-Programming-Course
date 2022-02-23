def announce(f):
    def wrapper():
        print("about to run the function")
        f()
        print("Done with running the function")
    return wrapper

@announce
def hello():
    print("hello world")

hello()