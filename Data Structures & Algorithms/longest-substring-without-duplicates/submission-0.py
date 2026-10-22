class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        start = 0
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                start = max (d[s[i]] + 1, start)
            d[s[i]] = i
            res = max(res, i - start + 1)
        return res
        