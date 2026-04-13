import heapq
from collections import Counter
class Solution(object):
    def reorganizeString(self, s):
        freq = Counter(s)
        
        maxHeap = []
        for ch in freq:
            heapq.heappush(maxHeap, (-freq[ch], ch))
        
        prev = (0, '')
        result = ""
        
        while maxHeap:
            count, ch = heapq.heappop(maxHeap)
            result += ch
            
            if prev[0] < 0:
                heapq.heappush(maxHeap, prev)
            
            count += 1  
            prev = (count, ch)
        
        if len(result) != len(s):
            return ""
        
        return result        