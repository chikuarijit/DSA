def is_valid(s: str) -> bool:
    stack = []
    closeToOpen = {")": "(", "}": "{", "]": "["}

    for c in s:
        if c in closeToOpen:
            if stack and stack[-1] is closeToOpen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False


s1 = "()"
s2 = "()[]{}"
s3 = "(]"
s4 = "([)]"
s5 = "{[]}"

print(is_valid(s1))  # Output will be True
print(is_valid(s2))  # Output will be True
print(is_valid(s3))  # Output will be False
print(is_valid(s4))  # Output will be False
print(is_valid(s5))  # Output will be True