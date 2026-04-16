import heapq
graph={
    "a":{"b":3,"c":4}
}
hurestic={
    "a":6,
    "b":5,
    "c":8
}
def gbfs(start,goal):
    visited=set()
    queue=[(hurestic[start],0,start,[])]

    while queue:
        h,cost,current,path=heapq.heappop(queue)
        if current==goal:
            path=path+[current]
            return path,cost
        if current not in visited:
            visited.add(current)
            path=path+[current]
            for x,y in graph.get(current,{}).items():
                heapq.heappush(queue,(hurestic[x],y+cost,x,path))
    return None,float("inf")
print(gbfs("a","b"))        

