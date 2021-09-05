#Create a class method named `validate`,
# which should be called from the `__init__` method to validate parameter email,passed to the constructor.
# The logic inside the `validate` method could be to check if the passed email parameter is a valid email string.

class Mail_valid:
    def __init__(self,address):
        if Mail_valid.validate(address):
            self.address = address

    def validate(address):
        if "@" not in address:
            print(' This is a not valid email address!No sumbol @')
            return False
        elif "." not in address:
            print(' This is a not valid email address!')
            return False
        elif "com" not in address:
            print(' This is a not valid email address!No "com"')
            return False
        print("This is a valid email address")
        return True


v = Mail_valid("sfdf@.com")


