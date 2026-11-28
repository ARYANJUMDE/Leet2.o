# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        result=[]
        def inorder(root,x,sum1):
            if root is None:
                return 
            x.append(root.val)
            sum1=sum1+root.val
            inorder(root.left,x,sum1)
            inorder(root.right,x,sum1)
            if root.left==None and root.right==None:
                if sum1==targetSum:
                    result.append(x[:])
            sum1=sum1-x[-1]
            x.pop()
        inorder(root,[],0)
        return result
            

        # from collections import deque
        # queue=deque([])
        # queue.append(root)
        # result=[]
        # while len(queue)>0:
        #     t=len(queue)
        #     x=[]
        #     sum1=0
        #     while t>0:
        #         o=queue.popleft()
        #         sum1=sum1+o.val
        #         if o.left!=None:
        #             queue.append(o.left)
        #         if o.right!=None:
        #             queue.append(o.right)
        #         t=t-1
        #     if sum1==targetSum:
        #         result.append(x)
        # return result


        