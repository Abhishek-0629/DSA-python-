# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def solve(node):
            if node is None:
                return [] 
            left=solve(node.left)
            right=solve(node.right)
            return left + [node.val]+right
        return solve(root)