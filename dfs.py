graph={
    "kudal":["kankavli","malvan","vengurla","sawantwadi"],
    "kankavli":["vaibhavwadi","kudal","devgad","malvan"],
    "sawantwadi":["kudal","dodamarg","vengurla"],
    "malvan":["devgad","kankavli","kudal","vengurla"],
    "vengurla":["malvan","kudal","sawantwadi"],
    "devgad":["kankavli","malvan"],
    "dodamarg":["sawantwadi"],
    "vaibhavwadi":["kankavli"]
}
visited=[]
def dfs(node,visited,graph):
    if node not in visited:
        print(node)
        visited.append(node)
        for i in graph[node]:
            dfs(i,visited,graph)

dfs('kudal',visited,graph)
