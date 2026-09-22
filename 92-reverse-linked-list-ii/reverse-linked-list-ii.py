# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        for i in range(left-1):
            prev=prev.next
        curr=prev.next

        for j in range(right-left):
            curr_node=curr.next
            curr.next=curr_node.next
            curr_node.next=prev.next
            prev.next=curr_node
        return dummy.next 


        