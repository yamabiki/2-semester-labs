def min_paint(k, t, lengths):
    max_length = max(lengths)
    total_length = sum(lengths)

    if k >= len(lengths):
        return max_length * t

    paint_per_worker = total_length / k
    return max(max_length, paint_per_worker) * t
