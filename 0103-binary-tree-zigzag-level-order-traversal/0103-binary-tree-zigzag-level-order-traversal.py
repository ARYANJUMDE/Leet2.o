# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        from collections import deque
        queue=deque([])
        queue.append(root)
        result=[]
        while len(queue)>0:
            t=len(queue)
            x=[]
            while t>0:
                p=queue.popleft()
                x.append(p.val)
                if p.left!=None:
                    queue.append(p.left)
                if p.right!=None:
                    queue.append(p.right)
                t=t-1
            result.append(x)
        o=[]
        for i in range(len(result)):
            if i%2==0:
                o.append(result[i])
            else:
                o.append(result[i][::-1])
        return o