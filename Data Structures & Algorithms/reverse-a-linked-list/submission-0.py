# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            # Save the next node in a temporary variable.
            next_temp = curr.next

            curr.next = prev

            # iterate to next node
            prev = curr
            curr = next_temp
        return prev
