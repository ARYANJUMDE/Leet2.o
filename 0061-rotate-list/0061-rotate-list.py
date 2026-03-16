# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head
        
        # find length
        length = 1
        tail = head
        
        while tail.next:
            tail = tail.next
            length += 1
        
        k = k % length
        if k == 0:
            return head
        
        # make circular list
        tail.next = head
        
        # find new tail
        steps = length - k
        newTail = head
        
        for i in range(steps-1):
            newTail = newTail.next
        
        # new head
        newHead = newTail.next
        
        # break circle
        newTail.next = None
        
        return newHead