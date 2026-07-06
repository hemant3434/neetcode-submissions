# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while slow:
            slow = slow.next
            if not fast or (not fast.next):
                break
            fast = fast.next.next
            if slow == fast:
                return True
        return False