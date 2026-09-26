class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        low = 0
        n = len(nums)
        high = n - 1
        for i in range(n):
            for j in range(i+1,n):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i,j]

        