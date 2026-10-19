class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        l=defaultdict(list)
        for i in strs:
            so=''.join(sorted(i))
            l[so].append(i)
        return list(l.values())