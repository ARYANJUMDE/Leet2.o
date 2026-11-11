# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        from collections import deque
        queue=deque([])
        queue.append(root)
        while len(queue)>0:
            result=[]
            y=len(queue)
            for i in range(y):
                x=queue.popleft()
                if x==None:
                    result.append(-99999)
                else:
                    result.append(x.val)
                    if x.left!=None:
                        queue.append(x.left)
                    elif(x.left==None):
                        queue.append(None)
                    if x.right!=None:
                        queue.append(x.right)
                    elif(x.right==None):
                        queue.append(None)
            if result[:len(result)//2]!=result[(len(result)+1)//2:][::-1]:
                return False
        return True


                


