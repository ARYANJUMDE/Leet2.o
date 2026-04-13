import heapq
from collections import defaultdict

class Solution(object):
    def networkDelayTime(self, times, n, k):
        graph = defaultdict(list)
        
        
        for u, v, w in times:
            graph[u].append((v, w))
        
        
        heap = [(0, k)]
        visited = set()
        max_time = 0
        
        while heap:
            time, node = heapq.heappop(heap)
            
            if node in visited:
                continue
            
            visited.add(node)
            max_time = max(max_time, time)
            
            for nei, wt in graph[node]:
                if nei not in visited:
                    heapq.heappush(heap, (time + wt, nei))
        
        
        return max_time if len(visited) == n else -1