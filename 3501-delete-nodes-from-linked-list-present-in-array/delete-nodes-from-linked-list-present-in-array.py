# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        seen=set(nums)
        while head and head.val in seen:
            head=head.next
        curr=head 
        while curr and curr.next:
            if curr.next.val in seen:
                curr.next=curr.next.next
            else:
                curr=curr.next
        return head 


