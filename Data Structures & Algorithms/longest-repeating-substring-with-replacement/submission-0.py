class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, res = 0, 0
        charDict = {}

        for end in range(len(s)):
            charDict[s[end]] = 1 + charDict.get(s[end], 0)

            while (end - start + 1) - max(charDict.values()) > k:
                charDict[s[start]] -= 1
                start += 1
            res = max(res, end - start + 1)

        return res