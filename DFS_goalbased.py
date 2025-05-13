from tree_input import input_tree

# DFS Function that stops when goal node is found
def dfs(tree, node, goal, visited=None, result=None):
    if visited is None:
        visited = set()
    if result is None:
        result = []

    visited.add(node)
    result.append(node)

    if node == goal:
        return True  # Found the goal node

    for child in tree.get(node, []):
        if child not in visited:
            found = dfs(tree, child, goal, visited, result)
            if found:
                return True  # Stop recursion if goal is found

    # Backtrack if this path doesn't lead to goal
    result.pop()  
    return False

# Input tree
tree = input_tree()

# Get start and goal node from user
start = input("Enter the start node (usually root): ")
goal = input("Enter the goal node to search for: ")

# Perform DFS
result_path = []
found = dfs(tree, start, goal, result=result_path)

print("\nDFS search result:")
if found:
    print("Path to goal node:")
    print(" -> ".join(result_path))
else:
    print(f"Goal node '{goal}' not found in the tree.")