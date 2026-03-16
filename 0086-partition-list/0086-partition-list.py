# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        beforeHead = ListNode(0)
        afterHead = ListNode(0)
        
        before = beforeHead
        after = afterHead
        
        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            
            head = head.next
        
        after.next = None
        before.next = afterHead.next
        
        return beforeHead.next
        