# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        k=[]
        while head:
            if head in k:
                return head
            else:
                k.append(head)
                head=head.next
        return None
        