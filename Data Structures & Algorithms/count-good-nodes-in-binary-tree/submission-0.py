# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        cnt = 0
        max_vals = { root: root.val }
        q = deque([(root, root.val)])

        while q:
            lvlLen = len(q)
            for i in range(lvlLen):
                cur, val = q.popleft()

                if cur.val >= val:
                    cnt += 1 
                
                cur_max = max(cur.val, val)

                if cur.left:
                    q.append((cur.left, cur_max))
                if cur.right:
                    q.append((cur.right, cur_max))
                    
        return cnt
        # def dfs(node, prt):
        #     nonlocal cnt
        #     nonlocal max_vals
        #     if node is None:
        #         return
            
        #     if not max_vals.get(prt):
        #         max_vals[node] = node.val
        #     else:
        #         if node.val > max_vals[prt]:
        #             cnt += 1
        #         max_vals[node] = max(node.val, max_vals.get(prt))

        #     dfs(node.left, node)
        #     dfs(node.right, node)
        
        # dfs(root, None)
        # print(max_vals)
        # return cnt
        