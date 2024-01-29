import sys

visited = [False]*9
graph = []
for i in range(9):
    list_1 = []
    list_1 = list(map(int,sys.stdin.readline().split()))
    graph.append(list_1)
    #print(graph[i])
def dfs(graph, v, visited):
    visited[v] = True
    print("v : "+str(v), end = '\n')
    print("visited[v] :  "+str(visited[v]))
    for i in graph[v]:
        print("i :  "+str(i))
        if not visited[i]:
            print("visited[i] :  "+str(visited[i])+", i :  "+str(i))
            dfs(graph, i, visited)

dfs(graph, 1, visited)
