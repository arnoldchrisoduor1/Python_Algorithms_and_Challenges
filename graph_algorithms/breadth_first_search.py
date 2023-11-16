from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        current_node = queue.popleft()
        if current_node not in visited:
            print(current_node, end='')
            visited.add(current_node)
            queue.extend(neighbor for neighbor in graph[current_node] if neighbor not in visited)