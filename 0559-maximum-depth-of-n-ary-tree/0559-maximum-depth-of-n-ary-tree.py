"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        from collections import deque
        queue=deque([])
        result=[]
        queue.append(root)
        while len(queue)>0:
            x=[]
            t=len(queue)
            while t>0:
                o=queue.popleft()
                x.append(o.val)
                for i in o.children:
                    queue.append(i)
                t=t-1
            result.append(x)
        return len(result)
        