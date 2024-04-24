# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        l=head
        k=[]
        while l:
            if l in k:
                return True
            else:
                k.append(l)
                l=l.next
        return False

        