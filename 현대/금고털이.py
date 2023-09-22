import sys

gold_list = []
money = 0
W, N = map(int, sys.stdin.readline().split())
# b:가격, a:무게
# for i in range(N):
#     a, b = map(int,sys.stdin.readline().split())
#     gold_list.append([b,a])
# gold_list= sorted(gold_list, key = lambda x: x[0])
# cnt = N
# while cnt > 0:
#     max_price = gold_list[cnt-1][0]
#     max_price_w = gold_list[cnt-1][1]
#     if W > max_price_w:
#         money+=max_price_w*max_price
#         W-=max_price_w
#         cnt-=1
#     elif max_price_w >= W:
#         money += max_price*W
#         break
# print(money)

for i in range(10001):
    gold_list.append(0)
# b:가격, a:무게
for i in range(N):
    a, b = map(int,sys.stdin.readline().split())
    gold_list[b] += a
for j in range(10000, 0, -1):
    if gold_list[j] != 0:
        if W > gold_list[j]:
            money+=gold_list[j]*j
            W-=gold_list[j]
        elif gold_list[j] >= W:
            money += j*W
            break
print(money)


# ######################################################################
# import sys
# input = sys.stdin.readline

# answer = 0

# W, N = map(int, input().split())

# metals = []

# for i in range(N):
#     metals.append(list(map(int, input().split())))

# metals = sorted(metals, key = lambda x:x[1], reverse = True)

# for metal in metals:
#     if metal[0] >= W:
#         answer += W * metal[1]
#         break
#     else:
#         answer += metal[0] * metal[1]
#     W -= metal[0]

# print(answer)