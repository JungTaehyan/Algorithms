S = list(input())
eng_list = ['a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
result = []
for i in eng_list:
    if i in S:
        result.append(S.index(i))
    elif i not in S:
        result.append(-1)
for j in result:
    print(j, end=' ')

# end = " " -> 다음 출력물을 한칸 띄고 같은 줄에 출력함