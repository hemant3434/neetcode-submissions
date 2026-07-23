class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(subset, i, total):
            if total == target:
                res.append(subset.copy())
                return
            if i == len(nums) or total > target:
                return
            
            subset.append(nums[i])
            dfs(subset, i,  total + nums[i])
            subset.pop()
            dfs(subset, i+1, total)

        
        dfs([], 0, 0)
        return res
        # result = []
        # dfs(com....)
        #     if sum(com) > target: stop
        #     if sum(com) == target: add to result if not seen before
        #     
        #     if sum is less than target:
        #     loop nums:
        #          add nums[i] to com and recurse