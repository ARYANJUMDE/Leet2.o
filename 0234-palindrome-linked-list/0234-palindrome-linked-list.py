# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        # fast=head
        # slow=head
        # while fast!=None and fast.next!=None:
        #     slow=slow.next
        #     fast=fast.next.next
        # mid=slow
        # curr=mid
        # prev=None
        # while curr!=None:

        #     save=curr.next
        #     curr.next=prev
        #     prev=curr
        #     curr=save
        # first=head
        # second=prev
        # while(second!=None):
        #     if(first.val!=second.val):
        #         return False
        #     second=second.next
        #     first=first.next
        # return True

        z=[]
        p=[]
        x=head
        x2=None
        q=head
        while x!=None:
            z.append(x.val)
            x=x.next
        while q!=None:
            t=q.next
            q.next=x2
            x2=q
            q=t
        y=x2
        while y!=None:
            p.append(y.val)
            y=y.next
        if(z==p):
            return(True)
        else:
            return(False)


        


        
        