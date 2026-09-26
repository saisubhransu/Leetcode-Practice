from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f1 = defaultdict(int)
        f2 = defaultdict(int)
        for i in s:
            f1[i] += 1
        for j in t:
            f2[j] += 1
        return f1 == f2        

        