from tree_input import input_tree 
 
def depth_limited_search(tree, current_node, limit, depth, visited, path):
    if depth > limit:
        return
   
    visited.add(current_node)
    path.append(current_node)
 
    for neighbor in tree.get(current_node, []):
        if neighbor not in visited:
            depth_limited_search(tree, neighbor, limit, depth + 1, visited, path)
 
def iterative_deepening_search(tree, root):
    limit_depth = 0 #initial Limit
    levels = {} #stores path for each level 
    total_nodes = set(tree.keys()).union(*tree.values()) #Keeps track fo each and every node in tree
    visited_total = set() #to check if each node is visited
 
    while len(visited_total) < len(total_nodes):
        visited = set()
        path = []
        depth_limited_search(tree, root, limit_depth, 0, visited, path)
       
        if path:
            levels[limit_depth] = path.copy()
            visited_total.update(visited)
       
        limit_depth += 1
 
    print("\nTREE TRAVERSING")
    print(f"TOTAL LEVEL OF TREE = {limit_depth - 1}")
    for lvl in range(limit_depth):
        if lvl in levels:
            print(f"LEVEL {lvl}: {' '.join(levels[lvl])}")
 
 
# Input tree
tree = input_tree()

# Input source node
start = input("Enter start node: ").strip()

# Perform IDDFS traversal on the full tree
iterative_deepening_search(tree, start)

print("\nIDDFS traversal completed.")