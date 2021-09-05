from functools import wraps

class TypeDecorators:

    @staticmethod
    def to_str(func):
        @wraps(func)
        def str_wrapp(string):
            return str(string)
        return to_str

    @staticmethod
    def to_int(func):
        @wraps(func)
        def int_wrapp(value):
            return int(value)
        return int_wrapp

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def bool_wrapp(value):
            return bool(value)
        return bool_wrapp

@TypeDecorators.to_int
def do_nothing(string: str):
    return string

@TypeDecorators.to_bool
def do_something(string: str):
     return string

assert do_nothing('25') == 25
assert do_something('True') is True
