from sys import stdin
n = stdin.readline()
N = sorted(map(int,stdin.readline().split()))
m = stdin.readline()
M = map(int, stdin.readline().split())
def binary_search(N, targetNum):
    start = 0
    end = len(N)-1 # index는 0부터 시작하기 때문
    while start <= end:
        midIndex = (start+end)//2 # 무한루프가 될 수 있어서 start+end로 함(범위가 계속 바뀌어야 하기 때문)
        indexValue = N[midIndex]
        if indexValue == targetNum:
            return 1
        elif indexValue < targetNum:
            start = midIndex + 1 # midIndex까지는 실행했으므로 +1 함
        elif indexValue > targetNum:
            end = midIndex - 1 # midIndex까지는 실행했으므로 -1 함
    return 0
for targetNum in M:
    print(binary_search(N, targetNum))
