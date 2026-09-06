# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        prev=None
        while curr:
            if curr.next and curr.val==curr.next.val:
                val=curr.val
                while curr and curr.val==val:
                    curr=curr.next
                if prev:
                    prev.next=curr
                else:
                    head=curr
            else:
                prev=curr
                curr=curr.next
        return head 
                
