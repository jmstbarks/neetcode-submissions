class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compDict = {}

        for index, value in enumerate(nums):
            comp = target - value
            if value in compDict:
                return [compDict[value], index]
            compDict[comp] = index