def lps_exec(needle):
    lps = [0] * len(needle)
    length = 0
    i = 1

    while i < len(needle):
        if needle[i] == needle[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

    return lps


def kmp_search(haystack, needle):
    if not needle:
        return "needle порожній"
    if len(needle) > len(haystack):
        return "needle довший ніж haystack"

    lps = lps_exec(needle)

    indexes = []
    i = 0
    j = 0

    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1

            if j == len(needle):
                indexes.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    if indexes == []:
        return "Індекси Відсутні"
    pass

    return indexes
