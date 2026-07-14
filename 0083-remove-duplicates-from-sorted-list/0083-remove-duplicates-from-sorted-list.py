# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        my=head
        while my.next:
            if my.val==my.next.val:
                my.next=my.next.next
            else:
                my=my.next
        return head
        