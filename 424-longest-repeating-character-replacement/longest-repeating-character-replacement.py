class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        low = 0
        high = 0
        n = len(s)
        res = -float('INF')
        f = [0] * 256
        for high in range(n):
            f[ord(s[high])] += 1
            l = high - low + 1
            m = max(f)
            diff = l - m
            while(diff > k):
                f[ord(s[low])] -= 1
                low += 1
                l = high - low + 1
                m = max(f)
                diff = l - m
            l = high - low + 1
            res = max(res,l)
        if res != -float('INF'):
            return res
        else:
            return 0        