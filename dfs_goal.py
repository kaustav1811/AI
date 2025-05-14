from tree_input import input_tree

def dfs(tree, node, goal, visited=None, path=None):
    if visited is None:
        visited = set()  
    if path is None:
        path = []  
    
    visited.add(node)
    path.append(node) 
    
    if node == goal:
        print("Path to goal node:", " -> ".join(path))
        return path 

    for child in tree.get(node, []):
        if child not in visited:
            result = dfs(tree, child, goal, visited, path)
            if result is not None: 
                return result

    path.pop()
    return None

tree = input_tree()

start = input("Enter the start node (usually root): ")
goal = input("Enter the goal node: ")

print("\nDFS traversal to reach the goal node:")
dfs(tree, start, goal)