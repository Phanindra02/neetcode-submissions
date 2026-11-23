class Solution:
    def trap(self, h: List[int]) -> int:
        if not h:
            return 0
        maxL,maxR=[0]*(len(h)),[0]*(len(h))
        lmax,rmax=0,0
        vol=0
        for i in range(1,len(h)):
            maxL[i]=max(lmax,h[i-1])
            lmax=max(maxL[i],lmax)
        for i in range(len(h)-2,-1,-1):
            maxR[i]=max(rmax,h[i+1])
            rmax=max(maxR[i],rmax)
        for i in range(len(h)):
            if min(maxL[i],maxR[i])-h[i]>=0:
                vol+=min(maxL[i],maxR[i])-h[i]
        return vol