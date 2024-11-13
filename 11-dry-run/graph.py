class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            self.add_node(node1)
        if node2 not in self.graph:  # Changed to `if`
            self.add_node(node2)

        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def get_neighbours(self, node):  # Fixed typo
        return self.graph.get(node, [])
    
    def has_edge(self, node1, node2):  # Minor rename for clarity
        return node2 in self.graph.get(node1, [])
    
    def print_graph(self):
        for node in self.graph:
            print(f'{node}: {self.graph[node]}')

def BFS(graph_dict, start_node):  # Accepts only the dictionary directly
    visited = []
    queue = [start_node]  # Initialize with start_node

    while queue:
        s = queue.pop(0)
        if s not in visited:
            print(s, end=' ')
            visited.append(s)

            for idx in graph_dict[s]:
                if idx not in visited:
                    queue.append(idx)

def DFS(graph_dict, start_node):
    visited = []
    stack = [start_node]  # Initialize with start_node

    while stack:
        s = stack.pop()
        if s not in visited:
            print(s, end=' ')
            visited.append(s)

            for idx in reversed(graph_dict[s]):
                if idx not in visited:
                    stack.append(idx)

# Example usage
if __name__ == '__main__':
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.print_graph()

    print("\nBFS:")
    BFS(g.graph, 1)
    print("\nDFS:")
    DFS(g.graph, 1)
