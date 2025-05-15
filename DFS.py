from tree_input import input_tree

# DFS Function for full traversal of the tree (recursive approach)
def dfs(tree, node, visited=None, result=None):
    if visited is None:
        visited = set()  # Initialize the visited set if it's the first call
    if result is None:
        result = []  # List to store the DFS traversal order
    
    # Mark the node as visited and add to the result list
    visited.add(node)
    result.append(node)  # Store the node
    
    # Recursively visit all the children (if any)
    for child in tree.get(node, []):
        if child not in visited:
            dfs(tree, child, visited, result)

    return result

# Input tree
tree = input_tree()

# Ask for start node (usually root)
start = input("Enter the start node (usually root): ")

# Perform DFS to traverse the tree
print("\nDFS traversal of the tree:")
result = dfs(tree, start)

# Join the result list with '->' and print it
print(" -> ".join(result))