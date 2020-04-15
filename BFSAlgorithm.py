class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = list()

        self.distance = 9999
        self.color = 'black'

    '''Getting letter name in vertex'''
    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()

class Graph:
    vertices = {}
    def add_vertex(self, vertex):
        if isinstance(vertex, vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] =vertex
            return True
        else:
            return False

