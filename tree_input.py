def input_tree():
    tree = {}
    num_nodes = int(input("Enter the number of nodes: "))
    
    print("Enter each node followed by its children (comma-separated):")
    for _ in range(num_nodes):
        parent = input("Enter node: ").strip()
        children_input = input(f"Enter children for node '{parent}' (comma-separated): ").strip()
        children = [child.strip() for child in children_input.split(',')] if children_input else []
        
        if parent in tree:
            tree[parent].extend(children)
        else:
            tree[parent] = children
            
    return tree