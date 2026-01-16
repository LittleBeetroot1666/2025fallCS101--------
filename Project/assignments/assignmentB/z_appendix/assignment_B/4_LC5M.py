class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        res = []
        lm = 0
        for i in range(n):
            for j in range(i, n + 1):
                if j - i >= lm:
                    if s[i: j] == s[i: j][:: -1]:
                        res.append(s[i: j])
                        lm = j - i
        return res[-1]
