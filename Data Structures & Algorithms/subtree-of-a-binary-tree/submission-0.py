# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        def isSame(t1, t2) -> bool:
            if (t1 is None) and (t2 is None):
                return True

            if ((t1 is None) and (t2 is not None)) or \
                ((t2 is None) and (t1 is not None)):
                return False
            
            if t1.val != t2.val:
                return False
            
            l = isSame(t1.left, t2.left)
            r = isSame(t1.right, t2.right)

            return l and r
        
        cur = isSame(root, subRoot)
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return cur or left or right

        
