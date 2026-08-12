class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        start, maxSub = 0, 0

        for end in range(len(s)):
            while s[end] in charSet:
                charSet.remove(s[start])
                start += 1
            maxSub = max(maxSub, end - start + 1)
            charSet.add(s[end])

        return maxSub
