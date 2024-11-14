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

    def has_neightbours(self, node):
        return self.graph.get(node, [])
    
    def has_edge(self, node1, node2):
        return node2 in self.graph.get(node1, [])
    
    def print_tree(self):
        for node in self.graph:
            print(f'{node}: {self.graph[node]}')


def BFS(graph_dict, start_node):
    visited = []
    queue = [start_node]

    while queue:
        s = queue.pop(0)
        if s not in visited:
            visited.append(s)

            for n in graph_dict[s]:
                if n not in visited:
                    queue.append(n)

    return visited

def DFS(graph_dict, start_node):
    visited = []
    stack = [start_node]

    while stack:
        s = stack.pop()
        if s not in visited:
            visited.append(s)

            for n in reversed(graph_dict[s]):
                if n not in visited:
                    stack.append(n)

    return visited

if __name__ == '__main__':
    g = Graph()

    g.add_node(1)
    g.add_node(2)

    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)

    g.print_tree()

    graph_dict = g.graph
    start_node = 1

    print(f'DFS: {DFS(graph_dict, start_node)}')
    print(f'BFS: {BFS(graph_dict, start_node)}')