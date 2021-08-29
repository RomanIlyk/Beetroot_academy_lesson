#Write a Python program to access a function inside a function (Tips: use function, which returns another function)
def test(a):
    def add(b):
        nonlocal a
        a += 1
        return a + b

    return add

func = test(1)
print(func(1))