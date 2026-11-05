class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = 0
        current = 0

        for num in nums:
            if num == 1:
                current += 1
                maxOnes = max(maxOnes, current)
            else:
                current = 0
        
        return maxOnes