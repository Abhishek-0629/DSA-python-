# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0 
        def dfs(node):
            nonlocal ans 
            if node is None:
                return 0,0
            leftsum,left_countsum=dfs(node.left)
            rightsum,right_countsum=dfs(node.right)
            total_sum=leftsum+node.val+rightsum
            total_count=1+left_countsum+right_countsum
            if node.val==total_sum//total_count:
                ans+=1
            return total_sum,total_count
        dfs(root)
        return ans 
