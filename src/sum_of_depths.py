class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def sum_of_depths(root, level):

    if root is None:
        return 0
    return (level + sum_of_depths(root.left, level + 1) +
            sum_of_depths(root.right, level + 1))
