import networkx as nx
import matplotlib.pyplot as plt

# Define the sets and the relation R
X = {'s', 't', 'x', 'y', 'z'}
Y = {'s', 't', 'x', 'y', 'z'}
R = {('s', 's'), ('s', 'x'), ('t', 'z'), ('y', 't'), ('z', 'y'), ('z', 'z')}

# Create a bipartite graph
G = nx.Graph()

# Add nodes from sets X and Y
G.add_nodes_from(X, bipartite=0)  # Set the 'bipartite' attribute to 0 for nodes in set X
G.add_nodes_from(Y, bipartite=1)  # Set the 'bipartite' attribute to 1 for nodes in set Y

# Add edges from relation R
G.add_edges_from(R)

# Draw the bipartite graph
pos = {node: (0 if node in X else 1, i) for i, node in enumerate(X.union(Y))}
nx.draw(G, pos=pos, with_labels=True, node_color=['red' if G.nodes[node]['bipartite'] == 0 else 'blue' for node in G.nodes])
plt.show()
