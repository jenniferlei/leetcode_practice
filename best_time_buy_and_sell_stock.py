# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# class Solution:
#     def stock_max_profit(self, prices) -> int:
#         """
#         return max profit from array of prices
#         parameter: prices (list of numbers)
#         return: number
#         """
    
#         # given [1, 2, 3, 4, 5] return 4
#         # given [5, 4, 3, 2, 1] return 0
    
#         # set max profit to 0
#         # set two pointers i and j
#         # brute force would go check profit for each num
#         max_profit = 0
    
#         # i, j = 0, 1
    
#         # while i < len(prices) - 1:
#         #     while j < len(prices):
#         #         profit = prices[j] - prices[i]
#         #         if profit > max_profit:
#         #             max_profit = profit
#         #         j += 1
#         #     i += 1
#         #     j = i + 1

#         for i in range(len(prices) - 1):
#             for j in range(i+1, len(prices)):
#                 profit = prices[j] - prices[i]
#                 if profit > max_profit:
#                     max_profit = profit

#         return max_profit


# solution = Solution()
# print(solution.stock_max_profit([1, 2, 3, 4, 5])) # 4
# print(solution.stock_max_profit([5, 4, 3, 2, 1])) # 0


class Solution:
    def stock_max_profit(self, prices) -> int:
        """
        return max profit from array of prices
        parameter: prices (list of numbers)
        return: number
        """
    
        # given [1, 2, 3, 4, 5] return 4
        # given [5, 4, 3, 2, 1] return 0
    
        # set max profit to 0
        # set two pointers l (left = index 0) and r (right = index i + 1)
        # while r is before end of prices
        # if right price > left price, check profit
            # if profit > max profit, set new max profit
            # shift right pointer
        # if right price < left price
            # shift left pointer to right pointer
            # shift right pointer
        
        
        max_profit = 0

        l, r = 0, 1

        while r < len(prices):
            if prices[r] >= prices[l]:
                profit = prices[r] - prices[l]
                if profit > max_profit:
                    max_profit = profit
            else:
                l = r
            r += 1
        

        return max_profit


solution = Solution()
print(solution.stock_max_profit([1, 2, 3, 4, 5])) # 4
print(solution.stock_max_profit([5, 4, 3, 2, 1])) # 0
print(solution.stock_max_profit([7,1,5,3,6,4])) # 5
