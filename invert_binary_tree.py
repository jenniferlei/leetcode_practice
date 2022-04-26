class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<{self.val} left: {self.left} right: {self.right}>"

# Given the root of a binary tree, invert the tree, and return its root.


def invert_tree(root):
    # two pointers, root left and root right
    # root left = root right, root right = root left
    # do this with root left and root right

    if not root:
        return None

    tmp = root.left
    root.left = root.right
    root.right = tmp

    invert_tree(root.left)
    invert_tree(root.right)

    return root


#             4
#         |        |
#         2        7
#       |   |    |   |
#       1   3    6   9

# [4,2,7,1,3,6,9]
node7 = TreeNode(9)
node6 = TreeNode(6)
node5 = TreeNode(3)
node4 = TreeNode(1)
node3 = TreeNode(7, node6, node7)
node2 = TreeNode(2, node4, node5)
node1 = TreeNode(4, node2, node3)

#             4
#         |        |
#         7        2
#       |   |    |   |
#       9   6    3   1

# [4,7,2,9,6,3,1]

print(invert_tree(node1))