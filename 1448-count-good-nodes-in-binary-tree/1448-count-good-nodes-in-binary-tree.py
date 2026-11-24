# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        x=[-9999999]
        max_count=0
        def preorder(root):
            nonlocal max_count
            if root is None:
                return
            if max(x)<=root.val:
                max_count=max_count+1
            x.append(root.val)
            preorder(root.left)
            preorder(root.right)
            x.pop()
        preorder(root)
        return max_count
        # from collections import deque
        # count=1
        # queue=deque([])
        # queue.append(root)
        # result=[]
        # while len(queue)>0:
        #     x=[]
        #     t=len(queue)
        #     while t>0:
        #         o=queue.popleft()
        #         if o==0:
        #             x.append(0)
        #         else:
        #             x.append(o.val)
        #             if o.left!=None:
        #                 queue.append(o.left)
        #             elif o.left==None:
        #                 queue.append(0)
        #             if o.right!=None:
        #                 queue.append(o.right)
        #             elif o.right==None:
        #                 queue.append(0)
        #         if x==[0,0]:
        #             break
        #         elif len(x)==2 and x!=[0,0]:
        #             result.append(x)
        #             x=[]
        #         t=t-1
        # return result
        # # for i in range(1,len(result)):
        #     for j in range(0,i):

        # for i in range(1,len(result)):
        #     if result[0]<=result[i]:
        #         count=count+1
        # return count
            
            
        