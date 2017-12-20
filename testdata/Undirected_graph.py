#!/usr/bin/env python
"""neteworkx_draw.py: nx.draw_networkx demonstration"""
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Make a graph.
G = nx.Graph()

# Define edges with weights.
G.add_weighted_edges_from(
    ((1, 2, 9.0),
        (1, 3, 13.0),
        (1, 4, 24.0),
        (1, 5, 17.0),
        (1, 6, 12.0),
        (1, 7, 6.0),
        (2, 4, 5.0),
        (2, 5, 5.0),
        (2, 6, 7.0),
        (2, 7, 9.0),
        (3, 4, 7.0),
        (3, 5, 9.0),
        (3, 6, 11.0),
        (3, 7, 10.0),
        (4, 5, 2.0),
        (4, 6, 1.0),
        (5, 6, 1.0),
        (5, 7, 3.0),))


#nodes = np.array(['user1', 'user2', 'user3', 'user4', 'user5', 'user6', 'user7'])
#G.add_nodes_from(nodes)
# Position nodes using Fruchterman-Reingold force-directed algorithm.
pos = nx.spring_layout(G,k=7.)

# Draw labels for nodes and edges.
nx.draw_networkx_labels(G, pos)

# Draw only weight attribute as edge label.
edge_labels = {(i, j): w['weight'] for i, j, w in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
edge_width = [ w['weight']*0.5 for i,j,w in G.edges(data=True)]
nx.draw_networkx_edges(G, pos, width=edge_width)

# Finish drawing.
nx.draw(G, pos)

# Display with Matplotlib.
plt.axis('off')
plt.show()