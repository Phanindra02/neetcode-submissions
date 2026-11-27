"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        temp=head
        copyHash={}
        while temp:
            copyHash[temp]=Node(temp.val)
            temp=temp.next
        
        temp=head
        while temp:
            copy=copyHash[temp]
            copy.next=copyHash.get(temp.next)
            copy.random=copyHash.get(temp.random)
            temp=temp.next
        return copyHash[head]