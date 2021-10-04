def areBracketsBalanced(string1):
    stack = []

    # Traversing the Expression
    for char in string1:
        if char in ["(", "{", "["]:

            # Push the element in the stack
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False

    # Check Empty Stack
    if stack:
        return False
    return True

if __name__ == "__main__":
    string1 = "({[()]})"

    # Function call
    if areBracketsBalanced(string1):
        print("Balanced")
    else:
        print("Not Balanced")