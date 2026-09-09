# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi=float('-inf')
        def solve(node):
            nonlocal maxi 
            if node is None:
                return 0 
            leftsum=solve(node.left)
            rightsum=solve(node.right)

            if leftsum<0:
                leftsum=0
            if rightsum<0:
                rightsum=0

            currsum=leftsum+node.val+rightsum
            maxi=max(maxi,currsum)
            return node.val+max(leftsum,rightsum)
        solve(root)
        return maxi 