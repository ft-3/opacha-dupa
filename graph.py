"""
For the vertices representation the keys are nodes, and the values
are adjacency lists. Looping over all nodes in the graph is done by
for v in G and looping over all neighbors simply by for u in G[v].
Edge weights need to be stored in a separate structure such that
weight[v][u] is the weight of the edge (v,u). Such a structure would
simply be a dictionary of dictionaries.
"""

from networkx.generators.random_graphs import erdos_renyi_graph
from random import randint

class graph:
    def __init__(self, size=5):
        # Generate random graph
        g = erdos_renyi_graph(10, 0.5)

        # Create our basic data structures
        self.vertices = {"v"+str(num): [] for num in g.nodes}
        self.weights = {"v"+str(num): {} for num in g.nodes}

        for edge in g.edges:
            # Create vertices dict
            self.vertices[f"v{edge[0]}"].append(f"v{edge[1]}")
            self.vertices[f"v{edge[1]}"].append(f"v{edge[0]}")

            # Weight dict
            rand_weight = randint(2, 10)
            self.weights[f"v{edge[0]}"][f"v{edge[1]}"] = rand_weight
            self.weights[f"v{edge[1]}"][f"v{edge[0]}"] = rand_weight

