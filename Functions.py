import ast
from Functions import *
from math import *

def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None

def Get_Graph():
    file = open('A_Star_Graph.txt','r')
    data = file.read()
    Graph_nodes = ast.literal_eval(data)
    # Sort The Graph Nodes By Key
    Graph_nodes = dict(sorted(Graph_nodes.items()))
    file.close()
    return Graph_nodes


# To Use The Distance Between Two Cities As Heuristic Function (Used lagitude and latitude To Calculate The Distance Instead )
# def Get_Heuristics():
#     file = open('heuristic_cities.txt','r')
#     data = file.read()
#     heuristics = ast.literal_eval(data)
#     file.close()
#     return heuristics

# def Heuristic_Cost(start_node, stop_node):
#     heuristics = Get_Heuristics()   
#     Node1 = heuristics[start_node]
#     for Node2 in Node1:
#         if Node2[0] == stop_node:
#             return Node2[1]
#     return None


#  lagitude and latitude functions
def Get_Longitude_Latitude():
    file = open('longitude_latitude_data.txt' ,'r')
    data = file.read()
    longitude_and_latitude = ast.literal_eval(data)
    file.close()
    return longitude_and_latitude

def Get_Heuristic_Distance(city1, city2):
    longitude_and_latitude = Get_Longitude_Latitude()
    city1 = longitude_and_latitude[city1]
    city2 = longitude_and_latitude[city2]
    R = 6373.0
    lat1 = radians(city1[0])
    lon1 = radians(city1[1])
    lat2 = radians(city2[0])
    lon2 = radians(city2[1])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance

def Get_Longitude_Latitude_List():
    Longitude_Latitude = Get_Longitude_Latitude()
    Longitude_Dic = []
    Latitude_Dic = []
    for key in Longitude_Latitude:
        Longitude_Dic.append(Longitude_Latitude[key][0])
        Latitude_Dic.append(Longitude_Latitude[key][1])
    return Longitude_Dic , Latitude_Dic



Graph_nodes = Get_Graph()


