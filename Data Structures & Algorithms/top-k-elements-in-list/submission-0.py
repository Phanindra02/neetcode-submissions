from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = dict(sorted(dict(Counter(nums)).items(), key=lambda item: item[1], reverse=True))
        l=list(c.keys())[:k]
        return l