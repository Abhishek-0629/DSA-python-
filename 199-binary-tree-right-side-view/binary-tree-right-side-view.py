# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        def dfs(node,level,ans):
            if node is None:
                return None
            if len(ans)==level:
                ans.append(node.val)
            if node.right:
                dfs(node.right,level+1,ans)
            if node.left:
                dfs(node.left,level+1,ans)
        ans=[]

        dfs(root,0,ans)
        return ans 
