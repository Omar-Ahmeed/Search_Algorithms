
from Functions import get_neighbors

def DFS(start_node, stop_node):
    stack = []
    stack.append(start_node)
    visited = []
    while len(stack) > 0:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n == stop_node:
                # print('Path found:', visited)
                return visited
            for (m,weight) in get_neighbors(n):
                stack.append(m)
    print('Path does not exist!')
    return None
