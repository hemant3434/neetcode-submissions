class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        print(candidates)
        # def dfs(cur_sum, cur_sub, index):
        #     print(f"{cur_sub} | ind: {index} | sum: {cur_sum}")
        #     if cur_sum == target:
        #         print(f"adding {cur_sub} because sum is {cur_sum}")
        #         res.append(cur_sub.copy())
        #         return

        #     if cur_sum > target or index >= len(candidates):
        #         return
            
        #     cur_sub.append(candidates[index])
        #     dfs(cur_sum + candidates[index], cur_sub, index + 1)

        #     cur_sub.pop()
        #     while index+1 < len(candidates) and candidates[index] == candidates[index + 1]:
        #         index += 1
        #     dfs(cur_sum, cur_sub, index+1)
        def dfs(idx, path, cur):
            if cur == target:
                res.append(path.copy())
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if cur + candidates[i] > target:
                    break

                path.append(candidates[i])
                dfs(i + 1, path, cur + candidates[i])
                path.pop()
        dfs(0, [], 0)
        return res