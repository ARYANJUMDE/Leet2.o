# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        from collections import deque
        result=set()
        queue=deque([])
        queue.append(root)
        while(len(queue))>0:
            x=queue.popleft()
            result.add(x.val)
            if x.left!=None:
                queue.append(x.left)
            if x.right!=None:
                queue.append(x.right)
        t=list(result)
        t.sort()
        return t[k-1]

