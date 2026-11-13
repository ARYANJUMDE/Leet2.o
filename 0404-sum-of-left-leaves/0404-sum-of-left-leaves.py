# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        result=[]
        from collections import deque
        queue=deque([])
        queue.append(root)
        while len(queue)>0:
            x=queue.popleft()
            if x.left!=None:
                queue.append(x.left)
                if x.left.left==None and x.left.right==None:
                    result.append(x.left.val)
            if x.right!=None:
                queue.append(x.right)
        return sum(result)
        