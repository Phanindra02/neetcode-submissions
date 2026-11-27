class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sl, fs = 0, 0

        while True:
            sl = nums[sl]
            fs = nums[nums[fs]]
            if sl == fs:
                break

        sl2 = 0
        while sl != sl2:
            sl = nums[sl]
            sl2 = nums[sl2]

        return sl