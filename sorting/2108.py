# import sys
# N = int(sys.stdin.readline().strip())
# list_1 = []
# for _ in range(N):
#     k = int(sys.stdin.readline().strip())
#     list_1.append(k)
# # 산술평균
# print(round(sum(list_1)/N))
# # 중앙값
# sort_1 = sorted(list_1)
# print(sort_1[N//2])
# # 최빈값
# mode_list = list(set(list_1))
# A = []
# for i in range(len(mode_list)):
#     a = list_1.count(mode_list[i])
#     A.append(a)
#
# b = []
# for j in range(len(A)):
#     if A[j] == max(A):
#         b.append(mode_list[j])
#
# if len(b) >= 2:
#     print(sorted(b)[1])
# else:
#     print(mode_list[0])
# # 범위
# print(sort_1[N-1]-sort_1[0])

import sys
from collections import Counter

n = int(sys.stdin.readline())
li = []
for _ in range(n):
    li.append(int(sys.stdin.readline()))

# 산술평균 - 다 더해서 / n
print(round(sum(li) / n))

# 중앙값 - 오름차순 -> 중간값
li.sort()
print(li[n // 2])

# 최빈값 - 빈출
cnt_li = Counter(li).most_common()
if len(cnt_li) > 1 and cnt_li[0][1] == cnt_li[1][1]:  # 최빈값 2개 이상
    print(cnt_li[1][0])
else:
    print(cnt_li[0][0])

# 범위 - 최댓값-최솟값
print(max(li) - min(li))