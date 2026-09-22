from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low = 0
        high = 0
        res = -float('INF')
        f = defaultdict(int)
        n = len(s)
        for high in range(n):
            f[s[high]] += 1
            k = high - low + 1
            while(len(f) < k):
                f[s[low]] -= 1
                if f[s[low]] == 0:
                    del f[s[low]]
                low+=1
                k = high - low + 1
            l = high - low + 1
            res = max(res,l)
        if res != -float('INF'):
            return res
        else:
            return 0                

        