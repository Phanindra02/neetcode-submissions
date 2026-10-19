class Solution:
    def maxProfit(self, p: List[int]) -> int:
        if len(p)==0:
            return 0
        buy=p[0]
        profit=0
        for i in range(1,len(p)):
            if buy>p[i]:
                buy=p[i]
            elif p[i]-buy>profit:
                profit=p[i]-buy
        return profit