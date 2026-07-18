# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(r1, r2) -> bool:
            if (not r1) and (not r2):
                return True
            
            if ((r1 is None) and (r2 is not None)) or ((r1 is not None) and (r2 is None)):
                return False
            
            if r1.val != r2.val:
                return False 

            l = dfs(r1.left, r2.left)
            r = dfs(r1.right, r2.right)

            return l and r

        return dfs(p, q)