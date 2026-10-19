class Solution:

    def encode(self, strs: List[str]) -> str:
        e = ""
        for s in strs:
            e += f"{len(s)}#{s}"
        return e

    def decode(self, s: str) -> List[str]:
        l = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            l.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return l