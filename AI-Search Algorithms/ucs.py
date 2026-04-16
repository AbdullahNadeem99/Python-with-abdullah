import heapq
graph={
    "A":{"b":3,"c":4}
}
def ucs(start,goal):
    cost=0
    path=[]
    visited=set()
    queue=[(cost,start,path)]

    while queue:
        cost,current,path=heapq.heappop(queue)
        if current==goal:
            path.append(current)
            return path,cost
        if current not in visited:
            path=path+[current]
            visited.add(current)
            for x,y in graph.get(current,{}).items():
                heapq.heappush(queue,(y+cost,x,path))
    return None,float("inf")
print(ucs("a","b"))
