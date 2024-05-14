# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        leng= self.lencheck(head)
        print(leng)
        if (leng < k):
            return head
        count=0
        prev_node = None
        current_node = head
        next_node=None

        while count < k and current_node is not None :
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
            count=count+1
        if next_node is not None:
            head.next= self.reverseKGroup(next_node,k)
        return prev_node
        
    def lencheck(self,head):
        c=0
        while head:
            c=c+1
            head= head.next
        return c

    def revlist(self,head):
        prev_node = None
        current_node = head

        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        return prev_node
        