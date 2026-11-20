# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        from collections import deque
        if root==None:
            return []
        queue=deque([])
        queue.append(root)
        result=[]
        while len(queue)>0:
            x=[]
            n=len(queue)
            while n>0:
                t=queue.popleft()
                if len(x)==0:
                    x.append(t.val)
                else:
                    if x[0]<t.val:
                        x[0]=t.val
                if t.left!=None:
                    queue.append(t.left)
                if t.right!=None:
                    queue.append(t.right)
                n=n-1
            result.append(x[0])
        return result
        