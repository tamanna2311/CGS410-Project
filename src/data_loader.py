import conllu
import networkx as nx

def load_conllu_trees(filepath):
    """
    Parses a conllu file and yields a networkx DiGraph for each valid dependency tree.
    Each node represents a token id. Edges are from head to dependent.
    Node 0 is the logical ROOT.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        data = f.read()

    sentences = conllu.parse(data)
    
    for sentence in sentences:
        G = nx.DiGraph()
        # Add root
        G.add_node(0, form='ROOT')
        
        valid_tree = True
        nodes_added = set([0])

        for token in sentence:
            # Skip multi-word tokens like '1-2' which are returned as tuples or lists
            if not isinstance(token['id'], int):
                continue

            node_id = token['id']
            head_id = token['head']
            
            # Form might be missing
            form = token['form'] if 'form' in token else str(node_id)
            
            G.add_node(node_id, form=form)
            nodes_added.add(node_id)
            
            if head_id is not None:
                # Add edge from head to dependent
                G.add_edge(head_id, node_id, deprel=token.get('deprel', ''))

        # Check if the tree is well-formed:
        # A valid dependency tree should have exactly N nodes and N-1 edges
        # and should be weakly connected without cycles.
        if nx.number_weakly_connected_components(G) != 1:
            valid_tree = False
        
        # In a directed tree, all nodes except root should have in-degree 1
        for n in G.nodes():
            if n == 0:
                if G.in_degree(n) != 0:
                    valid_tree = False
            else:
                if G.in_degree(n) != 1:
                    valid_tree = False
                    
        # Check for cycles
        if not nx.is_directed_acyclic_graph(G):
            valid_tree = False

        if valid_tree and len(G.nodes()) > 1:
            yield G
