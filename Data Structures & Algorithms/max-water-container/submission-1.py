class Solution:
    def maxArea(self, h: List[int]) -> int:
        l,r=0,len(h)-1
        maxVol=0
        while l<r:
            if h[l]<=h[r]:
                maxVol=max(maxVol,h[l]*(r-l))
                l+=1
            else:
                maxVol=max(maxVol,h[r]*(r-l))
                r-=1
        return maxVol