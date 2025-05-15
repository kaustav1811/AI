from collections import deque
from tree_input import input_tree

# BFS Function for full traversal of the tree
def bfs(tree, start):
    # Initialize the queue with the start node
    queue = deque([start])  # Queue stores nodes
    visited = set()  # Set to track visited nodes
    
    # Perform BFS loop
    result = []  # List to store the BFS traversal order
    while queue:
        # Dequeue a node from the front of the queue
        node = queue.popleft()
        
        # If the node hasn't been visited, process it
        if node not in visited:
            result.append(node)  # Add node to the result list
            visited.add(node)
            
            # Enqueue all unvisited neighbors of the current node
            for neighbor in tree.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)
    
    # Print the result list without trailing '->'
    #How it works :- " -> ".join(result) uses the string " -> " to join all elements of the list into a single string. It places " -> " between each element of the list. 
    print(" -> ".join(result))

# Input tree
tree = input_tree()

# Ask for start node (usually root)
start = input("Enter the start node (usually root): ")

# Perform BFS to traverse the tree
print("BFS traversal of the tree:- ",end = "")
bfs(tree, start)