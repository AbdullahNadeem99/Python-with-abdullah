import heapq
graph={
    "a":{"b":1,"c":3}
}
hurestic={
    "a":5,
    "b":6,
    "c":9
}
def a_star(start,goal):
    cost=0
    path=[]
    visited=set()
    queue=[(hurestic[start],cost,start,path)]
    while queue:
        f,cost,current,path=heapq.heappop(queue)
        if current==goal:
            path.append(current)
            return path,cost
        if current not in visited:
            path=path+[current]
            visited.add(current)
            for x,y in graph.get(current,{}).items():
                new_cost=y+cost+hurestic[x]
                heapq.heappush(queue,(new_cost,y+cost,x,path))
    return None,float("inf")
print(a_star("a","b"))
