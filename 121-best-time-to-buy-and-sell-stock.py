class Solution(object):
    def maxProfit(self, prices):
        l, r = 0, 1
        max_prof = 0

        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit >=0:
                max_prof = max(max_prof, profit)
            else:
                l = r
            r+=1

        return max_prof
