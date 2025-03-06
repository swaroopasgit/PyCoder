# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x=set()
        current = head
        previous = None
        while current:
            if current.val not in x:
                x.add(current.val)
                previous = current
            else:
                previous.next = current.next
            current=current.next

        return head