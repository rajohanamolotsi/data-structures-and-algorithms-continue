def DFS(graph, node):
    visited = []
    stack = []

    visited.append(node)
    stack.append(node)

    while stack:
        s = stack.pop()
        print(s, end=' ')

        for n in reversed(graph[s]):
            if n not in visited:
                visited.append(n)
                stack.append(n)