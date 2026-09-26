from collections import defaultdict
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        f = defaultdict(int)
        for i in nums:
            f[i] += 1
        return max(f,key=f.get)  

        