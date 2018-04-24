def verfy_strng(string):
    stack = []
    table = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
    for char in string:
        if not stack:
            stack.append(char)
        elif char not in table:
            stack.append(char)
        elif table[char] == stack[-1]:
            stack.pop()
        else:
            stack.append(char)
    if stack:
        print("NO")
    else:
        print("YES")    

number = int(input().strip())
for i in range(number):
    verfy_strng(input())
