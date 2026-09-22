class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        low = 0
        high = 0
        res = float('INF')
        sum = 0
        n = len(nums)
        while(high < n):
            sum += nums[high]
            while(sum >= target):
                l = high - low + 1
                res = min(res,l)
                sum -= nums[low]
                low += 1
            high += 1
        if res != float('INF'):
            return res
        else:
            return 0    