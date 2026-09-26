from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        f = defaultdict(int)
        for i in nums:
            f[i] += 1
        if len(nums) != len(f):
            return True
        else:
            return False        


        