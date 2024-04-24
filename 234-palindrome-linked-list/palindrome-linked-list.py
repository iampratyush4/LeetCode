# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l=[]
        pointer=head
        while pointer:
            l.append(pointer.val)
            pointer=pointer.next
        i=0
        ll=l.reverse()
        print(ll)
        while head:
            
            if l[i]== head.val:
                i=i+1
                head=head.next
                
            else:
                return False
        return True
        

        