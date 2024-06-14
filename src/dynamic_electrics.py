import math

def calculate_distance(width, height):
    return math.sqrt(width ** 2 + height ** 2)

def max_length(distance, heights):
    num_columns = len(heights)
    if num_columns == 1:
        return 0

    max_top_length = 0
    max_bottom_length = 0

    for i in range(num_columns - 1):
        bottom_to_bottom = distance
        height_difference = abs(heights[i] - heights[i + 1])
        max_to_max = calculate_distance(distance, height_difference)
        min_to_max = calculate_distance(distance, max(heights[i + 1] - 1, 0))
        max_to_min = calculate_distance(distance, max(heights[i] - 1, 0))

        next_top_length = max(max_to_max + max_top_length, min_to_max + max_bottom_length)
        next_bottom_length = max(max_to_min + max_top_length, bottom_to_bottom + max_bottom_length)

        max_top_length = next_top_length
        max_bottom_length = next_bottom_length




    return round(max(max_top_length, max_bottom_length), 2)