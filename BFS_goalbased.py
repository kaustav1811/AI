from collections import deque
from tree_input import input_tree

# BFS Function that stops when goal node is found
def bfs(tree, start, goal):
    queue = deque([start])
    visited = set()
    parent = {start: None}  # To reconstruct the path
    found = False

    while queue:
        node = queue.popleft()

        if node == goal:
            found = True
            break

        if node not in visited:
            visited.add(node)
            for neighbor in tree.get(node, []):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
                    parent[neighbor] = node  # Track path

    if found:
        # Reconstruct the path from goal to start
        path = []
        current = goal
        while current is not None:
            path.append(current)
            current = parent[current]
        path.reverse()

        print("Path to goal node:")
        print(" -> ".join(path))
    else:
        print(f"Goal node '{goal}' not found in the tree.")

# Input tree
tree = input_tree()

# Get start and goal node from user
start = input("Enter the start node (usually root): ")
goal = input("Enter the goal node to search for: ")

# Perform BFS to find goal node
print("\nBFS search result:")
bfs(tree, start, goal)