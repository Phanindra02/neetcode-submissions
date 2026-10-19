class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        r=0
        nums=list(sorted(set(nums)))
        l=[nums[0]]
        for i in range(1,len(nums)):
            if l[-1]==nums[i]-1:
                l.append(nums[i])
            else:
                r=len(l) if r<len(l) else r
                l=[nums[i]]
        return max(r,len(l))