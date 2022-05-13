# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if not root and not subroot, return True
        # if not subroot, return True
        # if root value != subroot value, check left node and check right node
        

        return

solution = Solution()

tree1 = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
subtree1 = TreeNode(4, TreeNode(1), TreeNode(2))

print(solution.isSubtree(tree1, subtree1))
# True

#   tree1      subtree1
#     3
#    / \
#   4   5        4
#  / \          / \
# 1   2        1   2

tree2 = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
subtree2 = TreeNode(4, TreeNode(1), TreeNode(2))

print(solution.isSubtree(tree2, subtree2))
# False

#   tree      subtree
#     3
#    / \
#   4   5        4
#  / \          / \
# 1   2        1   2
#    /
#   0