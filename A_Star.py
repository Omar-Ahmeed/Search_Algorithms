from Functions import Get_Graph , Get_Heuristic_Distance , get_neighbors

Graph_nodes = Get_Graph()

def A_Star(start_node, stop_node):
    heuristics = Get_Heuristic_Distance(start_node, stop_node)
    Open = set([start_node])
    Closed = set([])
    Distance = {}              
    parents = {}                

    Distance[start_node] = 0

    parents[start_node] = start_node
    while len(Open) > 0:
        n = None
  
        for v in Open:
            if n == None or Distance[v] + heuristics < Distance[n] + heuristics:
                n = v
        if n == stop_node or Graph_nodes[n] == None:
            pass
        else:
            for (m, weight) in get_neighbors(n):
  
                if m not in Open and m not in Closed:
                    Open.add(m)
                    parents[m] = n
                    Distance[m] = Distance[n] + weight

                else:
                    if Distance[m] > Distance[n] + weight:

                        Distance[m] = Distance[n] + weight

                        parents[m] = n
  
                        if m in Closed:
                            Closed.remove(m)
                            Open.add(m)
        if n == None:
            print('Path does not exist!')
            return None
        
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            # print('Path found:', path)
            return path
  
        Open.remove(n)
        Closed.add(n)
    print('Path does not exist!')
    return None