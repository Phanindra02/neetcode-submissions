# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        l=ListNode(0,l1)
        prev=l
        
        while l1 and l2:
            summ=(l1.val+l2.val+carry)
            l1.val=summ%10
            carry=summ//10
            l1=l1.next
            l2=l2.next
            prev=prev.next
        
        while l1:
            summ=l1.val+carry
            l1.val=summ%10
            carry=summ//10
            prev = l1
            l1=l1.next
        
        while l2:
            summ=l2.val+carry
            l2.val=summ%10
            carry=summ//10
            prev.next = l2
            l2=l2.next
            prev = prev.next
        
        if carry:
            prev.next=ListNode(carry)
            

        return l.next