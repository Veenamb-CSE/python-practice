class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = prices.copy()

        for i in range(0, len(prices)):

            for j in range(i + 1, len(prices)):

                if prices[j] <= prices[i]:

                    discount = prices[j]

                    answer[i] = prices[i] - discount

                    break

        return answer
        
