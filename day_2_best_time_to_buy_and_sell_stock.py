"""
Question

Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given
stock on the ith day.
You want to maximize your profit by choosing a single day to buy one
stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0
"""


def max_profit(prices):
    if not prices:
        return 0

    # Initialize variables to track the minimum price and maximum profit
    min_price = prices[0]
    maximum_profit = 0

    # Iterate through the prices array
    for price in prices:
        # Update the minimum price if a lower price is encountered
        min_price = min(min_price, price)

        # Calculate the potential profit if selling at the current price
        potential_profit = price - min_price

        # Update the maximum profit if a higher profit is found
        maximum_profit = max(maximum_profit, potential_profit)

    return maximum_profit


prices = [7, 1, 5, 3, 6, 4]
result = max_profit(prices)
print(result)
