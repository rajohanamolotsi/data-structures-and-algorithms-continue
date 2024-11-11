class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2):

        if node1 not in self.graph:
            self.add_node(node1)
        if node2 not in self.graph:
            self.add_node(node2)

        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def display_graph(self):
        for node in self.graph:
            print(f'{node}: {self.graph[node]}')

    def get_neighbours(self, node):
        return self.graph.get(node, [])
    
    def has_edges(self, node1, node2):
        return node2 in self.graph.get(node1, [])

if __name__ == '__main__':
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.display_graph()
    print(f'neighbours of node 1: {g.get_neighbours(1)}')
    print(f'Edges between 1, 3: {g.has_edges(1, 2)}')