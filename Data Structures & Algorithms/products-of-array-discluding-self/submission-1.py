import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        r=[0]*n
        suffix=[0]*n
        r[0]=suffix[-1]=1
        for i in range(1,n):
            r[i]=nums[i-1]*r[i-1]
        for i in range(n-2,-1,-1):
            suffix[i]=nums[i+1]*suffix[i+1]
            r[i]*=suffix[i]
        return r