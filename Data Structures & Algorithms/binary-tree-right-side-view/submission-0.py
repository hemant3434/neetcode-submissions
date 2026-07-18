# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        res = []
        def dfs(node, d):
            nonlocal res

            if not node:
                return
            
            # first node in depth
            if d == len(res):
                res.append(node.val)
            
            dfs(node.right, d + 1)
            dfs(node.left, d + 1)

        dfs(root, 0)
        return res

