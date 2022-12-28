 
from Functions import get_neighbors

def BFS(start_node, stop_node):
    queue = []
    queue.append(start_node)
    visited = []
    while len(queue) > 0:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            if n == stop_node:
                # print('Path found:', visited)
                return visited
            for (m,weight) in get_neighbors(n):
                queue.append(m)
    print('Path does not exist!')
    return None