class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        res = 0
        while(num > 0):
            last = num % 10
            res = (res * 10) + last
            num = num // 10
        if(res == x):
            return True
        else:
            return False        

           

        