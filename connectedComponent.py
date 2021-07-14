from disjointSet import disjointSet

def countComponents(self, n, edges):
    """
    Find the number of connected component in a graph.
    
    params:
        n: int, number of vertices in the graph
        edges: [[int, int], [int, int], ...], each nested list represents an edge
    """
    ds = disjointSet(n)
    # iterate over all edges
    for edge in edges:
        # join connected nodes
        ds.union(edge[0], edge[1])
    # check how many disjoint sets are there
    return len([x for x in range(len(ds.parent)) if ds.parent[x] == x])
