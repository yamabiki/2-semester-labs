def dfs(level, position, experience, hierarchy, max_experience):
    if level == len(hierarchy) - 1:
        max_experience[0] = max(
            max_experience[0], experience + hierarchy[level][position]
        )
        return

    dfs(
        level + 1,
        position,
        experience + hierarchy[level][position],
        hierarchy,
        max_experience,
    )
    dfs(
        level + 1,
        position + 1,
        experience + hierarchy[level][position],
        hierarchy,
        max_experience,
    )


def max_experience(hierarchy):
    max_exp = [0]
    dfs(0, 0, 0, hierarchy, max_exp)
    return max_exp[0]


with open("../test/career.in", "r") as f:
    L = int(f.readline())
    hierarchy = []
    for _ in range(L):
        hierarchy.append(list(map(int, f.readline().split())))

max_exp = max_experience(hierarchy)
with open("../test/career.out", "w") as f:
    f.write(str(max_exp))
