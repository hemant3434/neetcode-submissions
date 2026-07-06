"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:

        old_to_new = {}
        cur = head

        dummy = Node(0, None, None)
        prev = dummy
        # nh = Node(cur.val, None, None)
        # prev = nh
        # old_to_new[cur] = nh
        while cur:
            prev.next = Node(cur.val, None, None)
            prev = prev.next
            old_to_new[cur] = prev
            cur = cur.next
        
        cur = head
        prev = dummy.next
        while cur:
            if cur.random:
                prev.random = old_to_new[cur.random]
            prev = prev.next
            cur = cur.next

        return dummy.next
        