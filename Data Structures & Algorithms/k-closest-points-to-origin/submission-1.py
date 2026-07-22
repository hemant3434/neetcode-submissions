class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        eucd = lambda x: (x[0] ** 2) + (x[1] ** 2)

        def partition(l, r):
            #picking last index as pivot to hopefully be the "median"
            pivotIdx = r
            pivotDist = eucd(points[pivotIdx])
            i = l
            for j in range(l, r):
                if eucd(points[j]) <= pivotDist:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            points[i], points[pivotIdx] = points[pivotIdx], points[i]
            return i
        L, R = 0, len(points) - 1
        pivot = len(points)

        while pivot != k:
            pivot = partition(L, R)

            if pivot > k:
                R = pivot - 1
            else:
                L = pivot + 1
        return points[0:k]