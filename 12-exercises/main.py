from graph import Graph

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

def BFS_path_exists(graph_dict, start_node, end_node):
    visited = []
    queue = [start_node]

    while queue:
        s = queue.pop(0)
        if s == end_node:
            return True


        if s not in visited:
            visited.append(s)

            for n in graph_dict[s]:
                if n not in visited:
                    queue.append(n)

    return False

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

def BFS_shortest_path(graph_dict, start_node, end_node):
    visited = set()
    queue = [[start_node]]

    while queue:
        path = queue.pop(0)

        node = path[-1]

        if node == end_node:
            return path
        

        if node not in visited:
            visited.add(node)

            for n in graph_dict[node]:
                if n not in visited:
                    new_path = path + [n]
                    queue.append(new_path)

    return None


if __name__ == '__main__':
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)

    g.print_graph()

    print(f'BFS: {BFS(graph_dict=g.graph, start_node=1)}')
    print(f'DFS: {DFS(graph_dict=g.graph, start_node=1)}')
    print(f'BFS_path_exists: {BFS_path_exists(graph_dict=g.graph, start_node=1, end_node=4)}')
    print(f'BFS_shortest_path: {BFS_shortest_path(graph_dict=g.graph, start_node=3, end_node=4)}')