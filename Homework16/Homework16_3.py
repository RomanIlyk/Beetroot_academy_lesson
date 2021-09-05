#Create your own implementation of an iterable, which could be used inside for-in loop.
# Also, add logic for retrieving elements using square brackets syntax
class MyIterator:
    def __init__(self,start,stop,step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.stop:
            raise StopIteration
        else:
            value = self.start + self.step
            self.start += self.step
        return value

c = MyIterator(0,10,2)
for i in c:
    print(i)

