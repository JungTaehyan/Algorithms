while True:
    num = input().replace("", " ").split()
    # print(num[:len(num)//2])

    num_1 = num[len(num) // 2 + 1:]
    num_1.reverse()
    num_2 = num[len(num) // 2:]
    num_2.reverse()
    # print(num_1)
    # print(num_2)
    # print(num)
    if num[0] == '0' or num[0] == '':
        break
    elif num[:len(num)//2] == num_1:
        print('yes')
    elif num[:len(num)//2] == num_2:
        print('yes')
    else:
        print('no')