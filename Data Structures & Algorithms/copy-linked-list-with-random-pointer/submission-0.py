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
        oldto = {None : None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldto[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = oldto[cur]
            copy.next = oldto[cur.next]
            copy.random = oldto[cur.random]
            cur = cur.next

        return oldto[head] 