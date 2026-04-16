graph={
    "a":{"b":2,"c":3}
}
def dfs(start,goal):
    cost=0
    path=[]
    visited=set()
    queue=[(start,cost)]
    while queue:
        current,cost=queue.pop()
        if current==goal:
            path.append(current)
            return path,cost
        if current not in visited:
            path.append(current)
            visited.add(current)
            for x,y in reversed( graph.get(current,{}).items()):
                queue.append(x,y+cost)
    return None,float("inf")
print(dfs("a","b"))