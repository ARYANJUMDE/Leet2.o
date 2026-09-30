# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def maxLevelSum(self, root):
        result=[]
        queue=deque([])
        queue.append(root)
        while len(queue)>0:
            level=[]
            x=len(queue)
            for i in range(x):
                r=queue.popleft()
                level.append(r.val)
                if r.left!=None:
                    queue.append(r.left)
                if r.right!=None:
                    queue.append(r.right)
            result.append(sum(level))
        t=max(result)
        return result.index(t)+1
        
        


        