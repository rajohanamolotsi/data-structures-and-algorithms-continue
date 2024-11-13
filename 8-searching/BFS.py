def DFS(data, start, visited = set()):
    if start not in visited:
        print(start, end = ' ')

    visited.add(start)

    for idx in data[start] - visited:
        DFS(data, idx, visited)

    return

def BFS(data, start, visited = set()):
    queue = [start]

    while queue:
        current_node = queue.pop()
        if current_node not in visited:
            print(current_node, end= ' ')
        visited.add(current_node)
        for idx in data[current_node] - visited:
            queue.append(idx)

    return