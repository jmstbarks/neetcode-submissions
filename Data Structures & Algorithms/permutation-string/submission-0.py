class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1length, s2length = len(s1), len(s2)
        
        if s1length > s2length:
            return False

        s1Count = Counter(s1)
        s2Count = Counter(s2[:s1length])

        if s1Count == s2Count:
            return True

        start = 0

        for end in range(s1length, s2length):
            s2Count[s2[end]] += 1
            s2Count[s2[start]] -= 1

            start += 1

            if s1Count == s2Count:
                return True

        return False