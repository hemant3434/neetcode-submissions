class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        piv = nums[0]
        piv_index = 0

        while l <= r:
            if nums[l] < nums[r]:
                if nums[l] < piv:
                    piv_index = l
                    piv = nums[l]
                break

            m = (l + r) // 2
            print(f"m: {m} l: {l} r: {r}")
            if nums[m] < piv:
                piv = nums[m]
                piv_index = m

            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        print(f"pivot index: {piv_index} pivot: {piv} ")

        l_t, r_t = None, None
        if nums[piv_index] <= target <= nums[-1]:
            l_t, r_t = piv_index, (len(nums) - 1)
        else:
            l_t, r_t = 0, piv_index - 1

        print(f"l_t: {l_t} r_t: {r_t} ")

        while l_t <= r_t:
            m = (l_t + r_t) // 2

            if target == nums[m]:
                return m
            
            if target < nums[m]:
                r_t = m - 1
            else:
                l_t = m + 1
        return -1

        # return -1



