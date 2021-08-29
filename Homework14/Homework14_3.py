#Write a decorator `arg_rules` that validates arguments passed to the function.
def arg_rules(type_: type, max_length: int, contains: list):
     def wrapper(func):
         def wrapper_arg(name):
            if not isinstance(name, str):
               print('Is not a string')
               return False
            if len(name) > max_length:
              print('max_length constraint')
              return False
            for n in contains:
               if n not in name:
                  print('The necessary elements are missing')
                  return False
            return func(name)
         return wrapper_arg
     return wrapper

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan("S@SH05"))
assert create_slogan('johndoe05@gmail.com') is False  # -> Exceeded max_length constraint
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'



#create_slogan('')
#assert create_slogan('johndoe05@gmail.com') is False
#assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'