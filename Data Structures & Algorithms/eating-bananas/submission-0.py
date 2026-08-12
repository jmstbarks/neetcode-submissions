class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right

        while left <= right:
            time = 0
            mid = (left + right) // 2

            for p in piles:
                time += math.ceil(p/mid)

            if time <= h:
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1

        return res

            