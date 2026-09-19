class Solution:
    def sortColors(self, a: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        one = 0
        two = 0
        n = len(a)
        for i in range(0,n):
            if a[i] == 0:
                zero += 1
            elif a[i] == 1:
                one += 1
            else:
                two += 1
        a[:] = [0]*zero + [1]*one + [2]*two               


        