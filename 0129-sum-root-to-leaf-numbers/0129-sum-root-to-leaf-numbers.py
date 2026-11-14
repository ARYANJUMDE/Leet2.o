# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        x=[]
        def sum_leaf(root,st):
            if root is None:
                return
            if root.left is None and root.right is None:
                x.append(int(st+str(root.val)))
            sum_leaf(root.left,st+str(root.val))
            sum_leaf(root.right,st+str(root.val))
        sum_leaf(root,"")
        return sum(x)


            
        # from collections import deque
        # ans=[]
        # queue=deque([])
        # queue.append(root)
        # while len(queue)>0:
        #     result=[]
        #     n=len(queue)
        #     while n>0:
        #         x=queue.popleft()
        #         if x==-1:
        #             result.append(-1)
        #         else:
        #             result.append(x.val)
        #             if x.left!=None:
        #                 queue.append(x.left)
        #             else:
        #                 queue.append(-1)
        #             if x.right!=None:
        #                 queue.append(x.right)
        #             else:
        #                 queue.append(-1)
        #         n=n-1
        #     ans.append(result)
        # return ans


        