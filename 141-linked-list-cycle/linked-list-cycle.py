# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        f=s=head
        c=0
        if  head is None or head.next is None:
            return False
        while f and f.next:
            if f == s:
                if c==0:
                    c=c+1
                    f=f.next.next
                    s=s.next
                elif c>0:
                
                    return True
            else:
                f=f.next.next
                s=s.next
        return False








        # k=[]
        # while head:
        #     if head in k:
        #         return True
        #     else:
        #         k.append(head)
        #         head=head.next
        # return False

        