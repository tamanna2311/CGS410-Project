import networkx as nx
import numpy as np

def compute_metrics(G):
    """
    Computes structural metrics for a given directed graph G:
    - Max Arity (maximum out-degree)
    - Mean Arity (average out-degree)
    - Tree Depth (maximum shortest path length from root)
    - Graph Density (E / (V * (V - 1)) for directed graphs, though it'll be 1/V for trees)
    
    Assumes node 0 is the ROOT.
    """
    N = G.number_of_nodes()
    
    if N <= 1:
        return {
            'max_arity': 0,
            'mean_arity': 0,
            'tree_depth': 0,
            'density': 0.0
        }
        
    out_degrees = [d for n, d in G.out_degree()]
    max_arity = max(out_degrees)
    mean_arity = np.mean(out_degrees)
    
    # Calculate shortest paths from root to all reachable nodes
    try:
        lengths = nx.single_source_shortest_path_length(G, 0)
        tree_depth = max(lengths.values()) if lengths else 0
    except Exception:
        tree_depth = 0
        
    # Standard directed graph density: number of edges / possible edges
    density = nx.density(G)
    
    return {
        'max_arity': max_arity,
        'mean_arity': mean_arity,
        'tree_depth': tree_depth,
        'density': density
    }
