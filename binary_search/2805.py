from sys import stdin
N, M = map(int, stdin.readline().split())
tree_list = list(map(int, stdin.readline().split()))
start = 0
end = max(tree_list)
while start<=end:
    mid = (start+end)//2
    tree =0
    for i in tree_list:
        if i > mid:
            tree = tree + i - mid
    if tree >= M:
        start = mid+1
    else:
        end = mid - 1
print(end)


# 자르고 남은 나무의 길이가 M과 맞아 떨어지지 않을때를 고래해야함!!