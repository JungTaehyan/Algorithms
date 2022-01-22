test_case = int(input())
for i in range(test_case):
    score = 1
    total = 0
    list_1 = list(input())
    for i in list_1:
        if i == 'O':
            total += score
            score += 1
        else:
            score = 1

    print(total)
