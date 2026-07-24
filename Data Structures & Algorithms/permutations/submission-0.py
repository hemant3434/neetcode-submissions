class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        lBool = [False] * len(nums)
        def recursion():
            print(f"sub {sub}")
            if len(sub) == len(nums):
                # print(f"adding {sub}")
                res.append(sub.copy())
                return
            
            for i in range(len(nums)):
                if lBool[i] is False:
                    sub.append(nums[i])
                    lBool[i] = True
                    recursion()
                    lBool[i] = False
                    sub.pop()
                # else:

            # sub.append(nums[index])
            # lBool[index] = True
            # recursion(index + 1)


        
        recursion()
        return res