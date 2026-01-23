def maxProfit(prices: list[int]) -> int:
    """
    "Running Min/Max" Pattern:

    When you need to compare current element with previous elements
    But you only care about the best (min/max) seen so far
    Don't store all previous values—just track the running optimum
    """
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        # Update minimum buy price
        min_price = min(min_price, price)
        
        # Calculate profit if we sell today
        profit = price - min_price
        
        # Update maximum profit
        max_profit = max(max_profit, profit)
    
    return int(max_profit)