import numpy as np


#sample graph implemented as a dictionary

graph = {'A': ['B', 'S'],
         'B': ['A'],
         'C': ['D', 'E', 'F', 'S'],
         'D': ['C'],
         'E': ['C', 'H'],
         'F': ['C', 'G'],
         'G': ['F', 'H', 'S'],
         'H': ['E', 'G'],
         'S': ['A', 'C', 'G' ]}


Graph_Nodes = list(graph.keys())
explored = []
Q = []


start='A'
explored.append('A')
Graph_Nodes.remove(start)
print('Unvisited Nodes = ',Graph_Nodes)

print('******************')

current_working_node=start
print('Current Working Node = ',current_working_node)

while(len(Graph_Nodes)>0):
    nodes = graph.get(current_working_node)
    for val in nodes:
        if val not in explored and val not in Q:
            print('Enqueue ',val)
            Q.append(val)
    print('Queue Status=',Q)

    current_working_node = Q.pop(0)
    print('Current Working Node = ',current_working_node)
    print('Dequeue ', current_working_node)
    explored.append(current_working_node)
    Graph_Nodes.remove(current_working_node)
    print('Unvisted Nodes = ',Graph_Nodes)

print('Visited =',explored)
