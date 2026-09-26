class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_val = 0
        for i in accounts:
            res = sum(i)
            if res > max_val:
                max_val = res
        return max_val

        