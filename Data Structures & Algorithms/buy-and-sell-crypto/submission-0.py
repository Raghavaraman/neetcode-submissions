class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        base = 0
        profit = 0
        for i in range(1,len(prices)):
            temp = prices[i]-prices[base]
            if(temp < 0):
                base = i
            if(temp > profit):
                profit = temp
            i += 1
        return profit

        