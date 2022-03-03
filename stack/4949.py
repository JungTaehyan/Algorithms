while True :
    a = input()
    stack = []

    if a == "." :
        break

    for i in a :
        if i == '[' or i == '(' :
            stack.append(i)
        elif i == ']' :
            if len(stack) != 0 and stack[-1] == '[' :
                stack.pop() # 맞으면 지워서 stack을 비워줌 0 = yes
            else :
                stack.append(']')
                break
        elif i == ')' :
            if len(stack) != 0 and stack[-1] == '(' :
                stack.pop()
            else :
                stack.append(')')
                break
    if len(stack) == 0 :
        print('yes')
    else :
        print('no')



# while True:
#     a = input()
#     if a[0]==".":
#         break
#     b = []
#     for i in range(len(a)):
#         if a[i] == '(':
#             b.append('(')
#         elif a[i] == '[':
#             b.append('[')
#         elif a[i] == ')' and len(b)>0:
#             if b[len(b)-1]=='(':
#                 b.pop()
#         elif a[i] == ']'and len(b)>0:
#             if b[len(b) - 1] == '[':
#                 b.pop()
#         elif a[i] == ']' and len(b) == 0:
#             b.append(']')
#         elif a[i] == ')' and len(b) == 0:
#             b.append(')')
#     if len(b)>0:
#         print('no')
#     else:
#         print('yes')