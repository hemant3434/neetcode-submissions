# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True

        def dfs(root) -> int:
            nonlocal res
            if root is None:
                return 0
            
            l = dfs(root.left)
            r = dfs(root.right)

            h = 1 + max(l, r)

            if abs(l - r) > 1:
                res = False
            return h
        
        dfs(root)

        return res