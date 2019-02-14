# ハブ性のネットワーク図を作成するプログラム
# なお手作業で打ち込む模様(人,人,ハブ性スコア(正規化したものが望まれる))

#!/usr/bin/env python
"""neteworkx_draw.py: nx.draw_networkx demonstration"""
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Make a graph.
G = nx.Graph()

# Define edges with weights.
# G.add_weighted_edges_from(
#     ((1, 2, 9.0),(1, 3, 13.0),(1, 4, 24.0),(1, 5, 17.0),(1, 6, 12.0),(1, 7, 6.0),
#         (2, 4, 5.0),(2, 5, 5.0),(2, 6, 7.0),(2, 7, 9.0),(3, 4, 7.0),(3, 5, 9.0),(3, 6, 11.0),(3, 7, 10.0),
#         (4, 5, 2.0),(4, 6, 1.0),
#         (5, 6, 1.0),(5, 7, 3.0),))

G.add_weighted_edges_from(
    ((1, 2, 6.57),(1, 3, 5.76),(1, 4, 0.48),(1, 5, 0.76),(1, 7, 0.10),(1, 8, 9.86),(1, 9, 0.33),(1, 10, 0.81),(1, 12, 0.29),(1, 13, 4.81),(1, 14, 0.62),(1, 15, 1.14),(1, 16, 0.10),(1, 18, 0.19),(1, 19, 1.67),(1, 20, 1.19),(1, 21, 0.62),
        (2, 3, 1.67),(2, 4, 0.05),(2, 5, 0.05),(2, 7, 0.05),(2, 8, 0.76),(2, 10, 0.29),(2, 13, 0.14),(2, 14, 0.19),(2, 15, 0.14),(2, 16, 0.10),(2, 18, 0.10),(2, 19, 0.81),(2, 20, 0.29),(2, 21, 0.10),
        (3,8,0.52),(3,10,0.29),(3,13,0.05),(3,14,0.05),(3,16,0.05),(3,17,0.05),(3,19,0.10),(3,20,0.05),(3,21,0.05),
        (4,5,0.05),(5,8,0.05),(5,19,0.05),(7,8,0.05),(7,10,0.05),
        (8, 13, 0.14),(8, 14, 0.05),(8, 15, 0.10),(8, 16, 0.05),(8, 18, 0.05),(8, 19, 0.29),(8, 20, 0.19),(8, 21, 0.05),
        (13, 15, 0.05),(13, 20, 0.10),(13, 21, 0.05),
        (14,19,0.14),(14,20,0.05),(15, 19, 0.24),(15,20,0.29),(15,21,0.05),
        (18,19,0.1),(18,21,0.05),(19,20,0.05),
    )
)


#nodes = np.array(['user1', 'user2', 'user3', 'user4', 'user5', 'user6', 'user7'])
#G.add_nodes_from(nodes)
# Position nodes using Fruchterman-Reingold force-directed algorithm.
pos = nx.spring_layout(G,k=21.)

# Draw labels for nodes and edges.
nx.draw_networkx_labels(G, pos)

# Draw only weight attribute as edge label.
edge_labels = {(i, j): w['weight'] for i, j, w in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
edge_width = [ w['weight']*0.8 for i,j,w in G.edges(data=True)]
nx.draw_networkx_edges(G, pos, width=edge_width)

# Finish drawing.
nx.draw(G, pos)

# Display with Matplotlib.
plt.axis('off')
plt.show()