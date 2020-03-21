class graph:
    """
    For the vertices representation the keys are nodes, and the values
    are adjacency lists. Looping over all nodes in the graph is done by
    for v in G and looping over all neighbors simply by for u in G[v].
    Edge weights need to be stored in a separate structure such that
    weight[v][u] is the weight of the edge (v,u). Such a structure would
    simply be a dictionary of dictionaries.
    """
    def __init__(self, size=5):
        self.vertices = {
            "v1": [ "v2", "v3" ],
            "v2": [ "v1", "v3" ],
            "v3": [ "v1", "v2", "v4", "v5" ],
            "v4": [ "v3" ],
            "v5": [ "v3" ]
        }
        self.weights = {
            "v1": { "v2": 3, "v3": 4 },
            "v2": { "v1": 3, "v3": 5 },
            "v3": { "v1": 4, "v2": 5, "v4": 7, "v5": 2 },
            "v4": { "v3": 7 },
            "v5": { "v3": 2 }
        }

