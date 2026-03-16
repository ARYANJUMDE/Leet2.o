"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        
        if not head:
            return None
        
        oldToNew = {}
        
        curr = head
        
        # create copy of each node
        while curr:
            copy = Node(curr.val)
            oldToNew[curr] = copy
            curr = curr.next
        
        curr = head
        
        # assign next and random pointers
        while curr:
            copy = oldToNew[curr]
            
            copy.next = oldToNew.get(curr.next)
            copy.random = oldToNew.get(curr.random)
            
            curr = curr.next
        
        return oldToNew[head]
        