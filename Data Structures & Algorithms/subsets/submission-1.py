class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        def recursion(index):
            if index == len(nums):
                res.append(sub.copy())
                return
            sub.append(nums[index])
            recursion(index + 1)
            sub.pop()
            recursion(index + 1)
        
        recursion(0)
        return res