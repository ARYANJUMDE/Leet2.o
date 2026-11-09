# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        queue=deque([])
        queue.append(root)
        ans=[]
        while len(queue)>0:
            result=[]
            n=len(queue)
            for i in range(n):
                root=queue.popleft()
                result.append(root.val)
                if root.left!=None:
                    queue.append(root.left)
                if root.right!=None:
                    queue.append(root.right)
            ans.append(result)
        return ans[::-1]
        