def dijkstra(a,b):
    if a == b:
        return a
    elif a > b:
        return dijkstra(a-b,b)
    else:
        return dijkstra(b-a,a)
        
print(dijkstra(9,3))
print(dijkstra(9,6))
print(dijkstra(8,4))
print(dijkstra(8,5))