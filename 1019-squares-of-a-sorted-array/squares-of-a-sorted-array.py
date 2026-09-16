class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        pos = []
        neg = []
        res = []
        for i in nums:
            if i >= 0:
                pos.append(i)
            else:
                neg.append(i)    

        if (len(neg)==0):
            return [x**2 for x in pos] 

        if(len(pos)==0):
            res = [x**2 for x in neg]
            res.reverse()
            return res    

        neg = [x**2 for x in neg][::-1]
        pos = [x**2 for x in pos]
        n, m = len(neg), len(pos)

        i,j = 0,0

        while(i < n and j < m):
            if neg[i] <= pos[j]:
                res.append(neg[i])
                i += 1
            else:
                res.append(pos[j])
                j += 1          
        while (j < m):
            res.append(pos[j])
            j += 1
        while(i < n):
            res.append(neg[i])
            i += 1    
        return res      