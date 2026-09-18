class Solution:
    def threeSum(self, a: list[int]) -> list[list[int]]:
        a.sort()
        n = len(a)
        result = []
        for i in range(0,n-2):
            if i > 0 and a[i] == a[i-1]:
                continue
            else:
                left = i+1
                right = n-1
                sum = -1 * a[i]
                while(left < right):
                    s = a[left] + a[right]
                    if s == sum:
                        result.append([a[i],a[left],a[right]])
                        left += 1
                        right -= 1
                        while(left < n and a[left] == a[left-1]):
                            left += 1
                        while(right >= 0 and a[right] == a[right+1]):
                            right -= 1
                    elif s < sum:
                        left += 1
                    else:
                        right -= 1
        return result                                

        