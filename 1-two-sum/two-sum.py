from collections import defaultdict
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = defaultdict(int)
        for i,num in enumerate(nums):
            rem = target - num
            if rem in seen:
                return [seen[rem],i]
            seen[num] = i        

        