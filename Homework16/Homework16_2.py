#Create your own implementation of a built-in function range,
# named in_range(), which takes three parameters: `start`, `end`, and optional step
def in_range(start, end, step=2):
    n = [start]
    for i in range(start, end, step):
        start += step
        n.append((start))
    return n
print(in_range(0,20,2))
