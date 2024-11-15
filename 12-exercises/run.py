def BFS(graph_dicts, start_node):
    visited = []
    queue = [start_node]

    while queue:
        s = queue.pop(s)
        if s not in visited:
            visited.append(s)

            for n in graph_dicts[s]:
                if n not in visited:
                    queue.append(n)

    return visited

def BFS_path_exists(graph_dicts, start_node, end_node):
    visited = []
    queue = [start_node]

    while queue:
        s = queue.pop(0)

        if s == end_node:
            return True
        

        if s not in visited:
            visited.append(s)

            for n in graph_dicts[s]:
                if n not in visited:
                    queue.append(n)

    return False

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