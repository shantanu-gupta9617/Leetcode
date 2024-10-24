# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None or l2 is None:
            return l1 if l1 else l2
        
        head=temp=ListNode(0)
        while(l1 and l2):
            if(l1.val<l2.val):
                temp.next=l1
                l1.next
                temp.next
            else:
                temp.next=l2
                l2.next
                temp.next
        
        temp.next=l1 or l2
        return head

        
        
