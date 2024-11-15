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

    def has_neighbour(self, node):
        return self.graph.get(node, [])
    
    def has_edge(self, node1, node2):
        return node2 in self.graph.get(node1, [])
    
    def print_graph(self):
        for node in self.graph:
            print(f'{node}: {self.graph[node]}')