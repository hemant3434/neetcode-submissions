class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        uniq = set()
        def dfs(subset):
            nonlocal res, uniq
            cur_total = sum(subset)
            if cur_total > target:
                return
            if cur_total == target:
                tmp = tuple(sorted(subset))
                # print(f"found total with subset {frozenset(subset)}")
                if tmp not in uniq:
                    print(f"got inside {subset}")
                    res.append(subset.copy())
                    uniq.add(tmp)
                return
            
            for i in nums:
                subset.append(i)
                dfs(subset)
                subset.pop()
            
        
        dfs([])
        return res
        # result = []
        # dfs(com....)
        #     if sum(com) > target: stop
        #     if sum(com) == target: add to result if not seen before
        #     
        #     if sum is less than target:
        #     loop nums:
        #          add nums[i] to com and recurse