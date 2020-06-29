class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        discount=[]
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                if prices[j]<=prices[i]:
                    discount.append(prices[i]-prices[j])
                    break
            else:
                discount.append(prices[i])
        discount.append(prices[-1])
        return discount
