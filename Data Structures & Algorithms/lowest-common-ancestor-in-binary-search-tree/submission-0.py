# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None:
            return root
        
        res = None
        def lca(t, p, q):
            nonlocal res
            if t is None:
                return
            
            if p.val <= t.val <= q.val:
                res = t
            
            if q.val < t.val:
                lca(t.left, p, q)
            elif p.val > t.val:
                lca(t.right, p, q)
        if p.val < q.val:
            lca(root, p, q)
        else:
            lca(root, q, p)
        return res