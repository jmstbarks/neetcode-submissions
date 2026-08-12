class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqCount = {}

        for num in nums:
            freqCount[num] = 1 + freqCount.get(num, 0)

        bucketList = defaultdict(list)

        for num, freq in freqCount.items():
            bucketList[freq].append(num)

        res = []

        for i in range(len(nums), -1, -1):
            for num in bucketList[i]:
                res.append(num)

                if len(res) == k:
                    return res
