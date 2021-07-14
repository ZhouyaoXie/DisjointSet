# DisjointSet
An implementation of disjoint set in Python with path compression and union by rank.

### Time Complexity

- find & union: O(logn) worse case; O(a(n)) amortized worst case, where a(n) is the inverse Ackermann function

### Space Complexity

O(V), where V is the number of vertices

### Use Case

- connectedComponent.py: an example use case for finding the number of connected components in a graph
