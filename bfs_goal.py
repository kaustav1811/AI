from collections import deque
from tree_input import input_tree

def bfs(tree, start, goal):
    queue = deque([(start, [start])])
    visited = set()  
    
    while queue:
        node, path = queue.popleft()
        if node not in visited:
            visited.add(node)

            if node == goal:
                print("Path to goal node:", " -> ".join(path))
                return path  

            for neighbor in tree.get(node, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    print("Goal node not found.")
    return None 

tree = input_tree()

start = input("Enter the start node (usually root): ")
goal = input("Enter the goal node: ")

print("BFS traversal to reach the goal node:")
bfs(tree, start, goal)