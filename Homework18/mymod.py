#Basics, import, work with os module

def count_lines(Text18):
    f = open("Text18.txt", "r")
    print(len(f.readlines()))

#count_lines("Text18.txt")

def count_chars(Text18):
    f = open("Text18.txt", "r")
    print(len(f.read()))
#count_chars("Text18.txt")

def test (Text18):
    a = count_lines("Text18.txt")
    b = count_chars("Text18.txt")
test("Text18.txt")