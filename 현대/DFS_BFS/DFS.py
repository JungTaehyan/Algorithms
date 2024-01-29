import sys
ice_box = []
N, M = map(int, sys.stdin.readline().split())
for i in range(N):
    ice_box.append(list(map(int, sys.stdin.readline().split())))

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= M:
        return False
    if ice_box[x][y] == 0:
        ice_box[x][y] = 1

        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            result+=1
print(result)