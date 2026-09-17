# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        p = list1
        for __ in range(a-1):
            p=p.next
        q=p.next
        for __ in range(b-a+1):
            q=q.next
        p.next=list2
        while list2.next:
            list2=list2.next
        list2.next=q
        return list1
