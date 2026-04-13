class Solution(object):
    def findRedundantConnection(self, edges):
        parent = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # path compression
            return parent[x]

        def union(x, y):
            px = find(x)
            py = find(y)
            if px == py:
                return False  
            parent[px] = py
            return True

        
        for u, v in edges:
            parent[u] = u
            parent[v] = v

        
        for u, v in edges:
            if not union(u, v):
                return [u, v]    