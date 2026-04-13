from collections import deque

class Solution(object):
    def isBipartite(self, graph):
        n = len(graph)
        color = [-1] * n
        
        for i in range(n):
            if color[i] == -1:
                q = deque([i])
                color[i] = 0
                
                while q:
                    node = q.popleft()
                    
                    for nei in graph[node]:
                        if color[nei] == -1:
                            color[nei] = 1 - color[node]
                            q.append(nei)
                        elif color[nei] == color[node]:
                            return False
        return True