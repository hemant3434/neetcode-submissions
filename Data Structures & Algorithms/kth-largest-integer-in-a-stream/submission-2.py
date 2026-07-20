import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nh = nums
        heapq.heapify(nh)
        while len(nh) > k:
            heapq.heappop(nh)
        self.nh = nh

    def add(self, val: int) -> int:
        if len(self.nh) < self.k:
            heapq.heappush(self.nh, val)
            return self.nh[0]

        heapq.heappushpop(self.nh, val)
        # heapq.heappop(self.nh)
        return self.nh[0]
        #3,3,3,5,6,7,8
