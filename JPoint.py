# This class a graph
class Graph:

    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed

    # Add a link from A and B of given distance, and also add the inverse link if the graph is undirected
    def connect(self, A, B, distance=1):
        self.graph_dict.setdefault(A, {})[B] = distance

    # Get neighbors
    def get(self, a, b=None):
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)

    # Return a list of nodes in the graph
    def nodes(self):
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)

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
    # Create lists for open nodes and closed nodes
    opened = []
    closed = []

    # Create a start node and an goal node
    start_node = Node(start, None)
    goal_node = Node(end, None)

    opened.append(start_node)

    while len(opened) > 0:

        opened.sort()
        current_node = opened.pop(0)
        closed.append(current_node)

        # Check if we have reached the goal, return the path
        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node.name + '=>' + str(current_node.g))
                current_node = current_node.parent
            path.append(start_node.name + '=> ' + str(start_node.g))
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
            # add neighbor to open list
            opened.append(neighbor)
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