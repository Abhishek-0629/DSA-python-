# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0 
        def solve(node):
            if node is None:
                return 0,0 
            nonlocal ans 


            left_sum,left_count=solve(node.left)
            right_sum,right_count=solve(node.right)
            total_sum=left_sum+node.val+right_sum
            total_count=1+left_count+right_count

            if node.val==total_sum//total_count:
                ans+=1
            return total_sum,total_count
        solve(root)
        return ans 
       