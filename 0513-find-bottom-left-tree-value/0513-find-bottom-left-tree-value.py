# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        from collections import deque
        queue=deque([])
        queue.append(root)
        result=[]
        while len(queue)>0:
            x=[]
            t=len(queue)
            while t>0:
                p=queue.popleft()
                x.append(p.val)
                if p.left!=None:
                    queue.append(p.left)
                if p.right!=None:
                    queue.append(p.right)
                t=t-1
            result.append(x)
        return result[-1][0]