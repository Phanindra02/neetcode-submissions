# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head and not head.next:
            return 
        slow=fast=head
        while fast.next and fast.next.next:
            fast=fast.next.next
            slow=slow.next
        
        l=head
        r=slow.next
        slow.next=None
        
        prev=None
        while r:
            nxt=r.next
            r.next=prev
            prev=r
            r=nxt
        r=prev
        while l and r:
            l1=l.next
            r1=r.next
            l.next=r
            r.next=l1
            l=l1
            r=r1


        