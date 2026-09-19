# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode | None) -> TreeNode | None:
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next

        def bst(left,right):
            if left>right:
                return None 
            mid = (left+right)//2
            root=TreeNode(arr[mid])
            root.left=bst(left,mid-1)
            root.right=bst(mid+1,right)
            return root 
        return bst(0,len(arr)-1)



       # if head is None:
            #return None
        #def bst(head):
           #  slow=head
           # prev=None
           # while fast and fast.next:
               # prev=slow
            #    slow=slow.next
               # fast=fast.next.next
            #root=TreeNode(slow.val)

          #  if head==slow:
               # return head 
           # prev.next=None
          #  root.left=bst(head)
          #  root.right=bst(slow.next)
         #   return root 
       # return bst(head)
        