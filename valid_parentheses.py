def isValid(s):
    stack = []
    hash = { ")": "(" , "}":"{" , "]":"[" }

    for i in s:
        if stack and (i in hash and stack[-1] == hash[i]):
            stack.pop()
        else:
            stack.append(i)

    return not stack


s = input()
print(isValid(s))