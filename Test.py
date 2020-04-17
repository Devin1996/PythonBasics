'''The graph class represents to connect nodes in each node with given distance'''
class Graph:

    def __init__(self, graph_dir=None, directed=True):
        self.graph_dir = graph_dir or {}
        self.directed = directed
        if not directed:
            self.make_undirected()

    def make_undirected(self):
        for a in list(self.graph_dir.keys()):
            for (b, dist) in self.graph_dir[a].items():
                self.graph_dir.setdefault(b, {})[a] = dist

    '''Add a link from A and B of given distance and inverse link if the graph is undirected'''
    def connect(self, A, B, distance=1):
        self.graph_dir.setdefault(A, {})[B] = distance
        if not self.directed:
            self.graph_dir.setdefault(B, {})[A] = distance

    '''Get neighbors'''
    def get(self, a, b=None):
        link = self.graph_dir.setdefault(a, {})
        if b is None:
            return link
        else:
            return link.get(b)

    ''' Return a list of nodes in the graph '''
    def nodes(self):
        s1 = set([k for k in self.graph_dir.keys()])
        s2 = set([k2 for v in self.graph_dir.values() for k2, v2 in v.items()])
        node = s1.union(s2)
        return list(node)

'''The node class represents to nodes in each node '''
class Node:

    def __init__(self, name: str, parent: str):
        self.name = name
        self.parent = parent
        self.g = 0  # Distance to start node
        self.h = 0  # Distance to goal node
        self.f = 0  # Total cost

    # Compare nodes
    def __eq__(self, other):
        return self.name == other.name

    # Sort nodes
    def __lt__(self, other):
        return self.f < other.f

    # Print node
    def __repr__(self):
        return ('({0},{1})'.format(self.position, self.f))


# Best-first search
def best_first_search(graph, heuristics, start, end):
    # lists for opened nodes and closed nodes
    opened = []
    closed = []

    start_node = Node(start, None)
    goal_node = Node(end, None)

    # Add the start node
    opened.append(start_node)

    while len(opened) > 0:

        opened.sort()
        # Get the node with the lowest cost
        current_node = opened.pop(0)
        # Add the current node to the closed list
        closed.append(current_node)

        # Check if  reached the goal, return the path
        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node.name)
                current_node = current_node.parent
            path.append(start_node.name)
            # Return reversed path
            return path[::-1]

        # Get neighbours
        neighbors = graph.get(current_node.name)

        # Loop neighbors
        for key, value in neighbors.items():

            # Create a neighbor node
            neighbor = Node(key, current_node)

            # Check if the neighbor is in the closed list
            if (neighbor in closed):
                continue

            # Calculate cost to goal
            neighbor.g = current_node.g + graph.get(current_node.name, neighbor.name)
            neighbor.h = heuristics.get(neighbor.name)
            neighbor.f = neighbor.h

            # Check if neighbor is in open list and if it has a lower f value
            for node in opened:
                if (neighbor == node and neighbor.f > node.f):
                    continue

            # Everything is green, add neighbor to open list
            opened.append(neighbor)

    # Return None, no path is found
    return None

def main():
    # Create a graph
    graph = Graph()
    # distances between graphs
    graph.connect('S', 'A', 3)
    graph.connect('S', 'B', 2)
    graph.connect('A', 'C', 4)
    graph.connect('A', 'D', 1)
    graph.connect('B', 'E', 3)
    graph.connect('B', 'F', 1)
    graph.connect('E', 'H', 5)
    graph.connect('F', 'I', 2)
    graph.connect('F', 'G', 3)

    # heuristics
    heuristics = {}
    heuristics['S'] = 13
    heuristics['A'] = 12
    heuristics['B'] = 4
    heuristics['C'] = 7
    heuristics['D'] = 3
    heuristics['E'] = 8
    heuristics['F'] = 2
    heuristics['H'] = 4
    heuristics['I'] = 9
    heuristics['G'] = 0

    path = best_first_search(graph, heuristics, 'S', 'G')
    print(path)

if __name__ == "__main__": main()