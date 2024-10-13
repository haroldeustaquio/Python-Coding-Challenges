def max_subarray_sum(prices):
    for i in range(len(prices)):
        if prices[i] == min(prices):
            min_index = i

    return max(prices[min_index:]) - min(prices)
