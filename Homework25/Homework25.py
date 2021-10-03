#Task 1
from typing import Optional, Union

def to_power(x: Union[int, float], exp: int) -> Union[int, float]:
    if exp < 0:
        raise ValueError("This function works only with exp > 0.")
    if exp == 0:
        return 1
    return x * to_power(x, exp - 1)

#print(to_power(2.3, 4))
#print(to_power(2,-4))

#Task 2
def is_palindrome(looking_str: str) -> bool:
    if len(looking_str) < 2:
        return True

    looking_str = looking_str.lower()
    if looking_str[0] != looking_str[-1]:
        return False

    return is_palindrome(looking_str[1:-1])

#print(is_palindrome('Sassas'))
#print(is_palindrome('mom'))
#print(is_palindrome('o'))
#Task 3
def mult(a: int, n: int) -> int:

    if a < 0 or n < 0:
        raise ValueError('This function works only with positive integers')
    if n == 0:
       return a
    else:
       return a + mult(a, n-1)

# print(mult(2, 4) == 8)
# print(mult(2, 0) == 0)
# print(mult(2, -4) == 0)

#Task 4
def reverse(input_str: str) -> str:
    if len(input_str) == 0:
        return input_str
    return reverse(input_str[1:]) + input_str[0]

print(reverse('hello'))
print(reverse('o'))


