import sys
# A = int(sys.stdin.readline())
# cnt = 0
# list_1 = []
# b=''
# while cnt < A:
#     string_1 = sys.stdin.readline()
#     string_1 = string_1.replace('\n','')
#     list_1.append(string_1)
#     cnt += 1
# list_1 = list(set(list_1))
# list_1 = sorted(list_1)
#
# # for i in range(len(list_1)-1):
# #     for j in range(i+1, len(list_1)):
# #         if len(list_1[i]) > len(list_1[j]):
# #             b = list_1[j]
# #             list_1[j] = list_1[i]
# #             list_1[i] = b
# #         elif len(list_1[i]) == len(list_1[j]):
# #             if list_1[i] > list_1[j]:
# #                 b = list_1[j]
# #                 list_1[j] = list_1[i]
# #                 list_1[i] = b
# for n in list_1:
#     print(n)

input = sys.stdin.readline
N = int(input())
words = []
for _ in range(N):
    word = input().strip()
    words.append([len(word), word])

words.sort(key=lambda x: (x[0], x[1]))
words = [word[1] for word in words]

sorted_words = []

for word in words:
    if word not in sorted_words:
        sorted_words.append(word)

for word in sorted_words:
    print(word)

