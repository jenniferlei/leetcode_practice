# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

#         1
#     2        3
#   4    5

# [4, 2, 1, 3] -> 3
# [5, 2, 1, 3] -> 3

#       1
#      / \
#     2   3
#    / \
#   4   5
#      / \
#     6   7
#    / \
#   8   9
[1,2,3,4,5,None,None,None,None,6,7,8,9]

# [3, 1, 2, 5, 6, 8] -> 5
# [3, 1, 2, 5, 6, 9] -> 5


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameter_binary_tree(root):
    # get max levels on left and max levels on right
    # add up the levels

    diameter = 0

    def DFS(root):
        nonlocal diameter
        
        if not root:
            return 0

        # recursively go down to the lowest nodes to get height of node
        left = DFS(root.left) # get height of left node
        right = DFS(root.right) # get height of right node

        diameter = max(diameter, left + right) # set diameter to max between current diameter and current nodes diameter

        return max(left, right) + 1 # returns nodes max height (either left or right height)

    DFS(root) # go through each node recursively
    return diameter