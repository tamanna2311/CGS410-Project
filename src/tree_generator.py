import networkx as nx
import random

def generate_random_dag(num_nodes):
    """
    Generates a random directed tree (DAG) with the exact same number of nodes.
    This uses networkx.random_tree to generate a uniformly random undirected tree,
    and then directs all edges outwards from a randomly chosen root node (0).
    The generated DAG will have nodes labeled 0 to num_nodes - 1.
    """
    if num_nodes <= 1:
        G = nx.DiGraph()
        G.add_node(0, form='ROOT')
        return G
        
    # Generate a random undirected tree
    # nx.random_tree returns a random uniformly chosen labeled tree
    U = nx.random_tree(num_nodes)
    
    # We choose node 0 to be the root.
    root = 0
    
    # We will build the directed graph outwards from the root
    D = nx.DiGraph()
    D.add_nodes_from(U.nodes())
    D.nodes[root]['form'] = 'ROOT'
    
    # BFS to direct edges
    visited = set([root])
    queue = [root]
    
    while queue:
        current = queue.pop(0)
        # For all neighbors of current in undirected tree
        for neighbor in U.neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                D.add_edge(current, neighbor)
                queue.append(neighbor)
                
    return D
