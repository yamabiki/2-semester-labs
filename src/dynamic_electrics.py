import math


def max_length(width, heights):
    num_heights = len(heights)
    dp = [[0] * (h + 1) for h in heights]


    for height in range(1, heights[0] + 1):
        dp[0][height] = 0
    for i in range(1, num_heights):
        for height2 in range(1, heights[i] + 1):
            dp[i][height2] = max(
                dp[i - 1][height1] + calculate_distance(width, height1, height2)
                for height1 in range(1, heights[i - 1] + 1)
            )

    max_length = max(dp[-1])


    return round(max_length, 2)


def calculate_distance(width, height1, height2):
    return math.sqrt(width ** 2 + (height2 - height1) ** 2)


