from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        low = 0
        high = 0
        f = defaultdict(int)
        n = len(fruits)
        res = -float('INF')
        for high in range(n):
            f[fruits[high]] += 1
            while len(f) > 2 :
                f[fruits[low]] -= 1
                if f[fruits[low]] == 0:
                    del f[fruits[low]]
                low += 1
            if len(f) == 2 or len(f) < 2:
                l = high - low + 1
                res = max(res,l)
        if res != -float('INF'):
            return res
        else:
            return 0                    



        