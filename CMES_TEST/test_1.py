# 일반 input()보다 입력 시간이 빠르기 때문에 sys 모듈의 stdn을 활용하였습니다.
from sys import stdin
# 수열을 입력 받을때 정수의 갯수가 각각 N개와 M개가 아닐 시 예외처리를 하였습니다.
N = int(stdin.readline())
while True:
    line_1 = stdin.readline().split()
    if len(line_1) != N:
        print("정수의 갯수가 올바르지 않습니다. 다시 입역해주세요.")
    else:
        break
M = int(stdin.readline())
while True:
    line_2 = stdin.readline().split()
    if len(line_2) != M:
        print("정수의 갯수가 올바르지 않습니다. 다시 입력해주세요.")
    else:
        break
# 수열에 포함되는지 아닌지에 대한 데이터를 저장하기 위해 변수를 생성하였습니다.
answer = []
# line_2의 데이터를 하나씩 가져와 line_1에 있다면 1, 없으면 0을 answer에 저장합니다.
for i in line_2:
    if i in line_1:
        answer.append(1)
    else:
        answer.append(0)
# answer에 저장된 데이터를 하나씩 출력합니다.
for j in answer:
    print(j)