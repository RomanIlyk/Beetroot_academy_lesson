#Write a decorator that prints a function with arguments passed to it.
#NOTE! It should print the function, not the result of its execution!
def logger(func):
    def wrapper(*args):
        print(f'function {func.__name__} ', end="")
        print(*args)
        func(*args)
    return wrapper

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


add(3, 5)
square_all(3, 4, 5)