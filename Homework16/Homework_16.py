#Create your own implementation of a built-in function enumerate,
# named `with_index`, which takes two parameters: `iterable` and `start`, default is 0.
def with_index(iterable,start=0):
    n = []
    for i in iterable:
        n.append((start,i))
        start += 1
    return n

list1=['sss',13,9,'ttt','rrr', 21]
print(with_index(list1))
