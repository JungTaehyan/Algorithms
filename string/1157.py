str_1 = input().upper()
str_1 = str_1.replace('', ' ')
str_1 = str_1.split()
str_set = set(str_1)
str_set = list(str_set)
str_set.sort()
a = []
b = 0
for i in str_set:
    b = int(str_1.count(i))
    a.append(b)

if int(a.count(max(a))) >= 2:
    print("?")
else:
    print(str_set[int(a.index(max(a)))])


# upper(), sort(), append(), set()->집합(중복제거할 때 사용함), replace("", "+") 사용법 숙지하기

