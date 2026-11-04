class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for i in strs:
            if ''.join(sorted(i)) not in d.keys():
                d[''.join(sorted(i))]=[i]  
            else:
                d[''.join(sorted(i))].append(i)
        return list(d.values())