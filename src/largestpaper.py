def find_square(n, w, h):
    i = 1
    j = max(w, h) * n
    while i < j:
        mid = i + (j - i) // 2
        if check_capacity(w, h, n, mid):
            j = mid
        else:
            i = mid + 1
    return j


def check_capacity(w, h, n, x):
    val = (x // w) * (x // h)
    if val >= n:
        return True
    else:
        return False


