class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        a = 0
        res = 1
        b = 1
        while (b < n):
            if nums[b] == nums[b-1]:
                b+=1
            elif nums[b] != nums[b-1]:
                res += 1
                nums[a+1] = nums[b]
                a += 1
                b += 1

        return res            
        