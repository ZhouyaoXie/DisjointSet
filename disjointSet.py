class disjointSet:

    def __init__(self, n):
        """
        Initialize a disjoint set object.
        
        params:
            n: size of the disjoint set
            
        """
        self.rank = [1 for _ in range(n)]
        self.parent = list(range(n))

    def union(self, x, y):
        """
        Union the set that x is in with the set y is in
        """
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            # union by rank: always attach the smaller set to the larger set
            if self.rank[s1] > self.rank[s2]:
                self.parent[s2] = s1
                self.rank[s1] += self.rank[s2]
            else:
                self.parent[s1] = s2
                self.rank[s2] += self.rank[s1]

    def find(self, x):
        """
        Find the set that x belongs.

        Returns:
            the root (head) of the set that x is in
        """
        if self.parent[x] != x:
            # path compression
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
