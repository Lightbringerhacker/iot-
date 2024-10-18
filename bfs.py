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
queue=[]
def bfs(node,visited,graph):
    visited.append(node)
    queue.append(node)
    while queue:
        m=queue.pop(0)
        print(m,end=' ')
        for i in graph[m]:
            if i not in visited:
                visited.append(i)
                queue.append(i)

bfs('kudal',visited,graph)
