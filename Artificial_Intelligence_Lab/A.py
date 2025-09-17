import heapq

# Graph
graph = {
    'S': {'A': 1, 'B': 4},
    'A': {'B': 2, 'C': 5, 'D': 12},
    'B': {'C': 2},
    'C': {'D': 3, 'G': 7},
    'D': {'G': 2},
    'G': {}
}

# Heuristics
heuristics = {
    'S': 7, 'A': 6, 'B': 4,
    'C': 2, 'D': 1, 'G': 0
}

def a_star_search(start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristics[start], 0, start, [start]))
    closed = set()

    while open_list:
        f, g, node, path = heapq.heappop(open_list)

        if node == goal:
            return path, g

        if node in closed:
            continue
        closed.add(node)

        for neighbor, cost in graph[node].items():
            g_new = g + cost
            f_new = g_new + heuristics[neighbor]
            heapq.heappush(open_list, (f_new, g_new, neighbor, path + [neighbor]))

    return None, float("inf")

# Run A*
start, goal = 'S', 'G'
path, cost = a_star_search(start, goal)
print("Optimal Path:", path)
print("Total Cost:", cost)


