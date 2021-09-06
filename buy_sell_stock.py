"""
    buy-sell stock
    [7, 1, 5, 3, 6, 4] ==> 5
    [9, 7, 6, 4, 3, 1] ==> 0
"""


def max_profit(prices):
    cur_max, final_max = 0, 0

    for i in range(1, len(prices)):
        cur_max = max(0, cur_max + prices[i] - prices[i - 1])
        final_max = max(cur_max, final_max)

    return final_max


max_profit([7, 1, 5, 3, 6, 4])
