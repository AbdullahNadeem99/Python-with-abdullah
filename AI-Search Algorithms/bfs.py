graph={
    "A":{"b":3,"c":4},
    "d":{"e":4,"f":5}
}
def bfs(start,goal):
    cost=0
    path=[]
    visited=set()
    queue=[(start,cost)]

    while queue:
        current,cost=queue.pop(0)
        if current==goal:
            path.append(current)
            return path,cost
        if current not in visited:
            path.append(current)
            visited.add(current)
            for x,y in graph.get(current,{}).items():
                queue.append((x,y+cost))
    return None,float("inf")
print(bfs("A","b"))

    