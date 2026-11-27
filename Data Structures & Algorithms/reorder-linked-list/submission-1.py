# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        r = self._split_at_middle(head)
        r = self._reverse(r)
        self._merge(head, r)

    def _split_at_middle(self, head: ListNode) -> Optional[ListNode]:
        slow = fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        r = slow.next
        slow.next = None
        return r

    def _reverse(self, r: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while r:
            nxt = r.next
            r.next = prev
            prev = r
            r = nxt
        return prev

    def _merge(self, l: Optional[ListNode], r: Optional[ListNode]) -> None:
        while l and r:
            l1 = l.next
            r1 = r.next
            l.next = r
            r.next = l1
            l = l1
            r = r1