# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None:
            return False
        if head.next==None:
            return False
        slow=fast=head

        while fast!=None:
            if fast.next==None:
                return False
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                return True
        return False