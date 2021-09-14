#Create your own class, which can behave like a built-in function `open`.
# Also, you need to extend its functionality with counter and logging.

class File(object):

    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
        print("File open")

    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        self.file_obj.close()
        print("File close")

def write(text: str):
    with File('demo.txt', 'w') as opened_file:
     opened_file.write(f'{text}\n')

def read(file: str):
    with File('demo.txt', 'r+') as read_file:
        f = read_file.read()
        print(f)

#write('Hello world')
read('demo.txt')