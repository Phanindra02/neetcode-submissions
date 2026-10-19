class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        h=defaultdict(int)
        for i in range(len(num)):
            d=target-num[i]
            if h[d]:
                return [h[d], i+1]
            h[num[i]]=i+1
        return []