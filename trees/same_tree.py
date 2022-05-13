# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def same_tree(self, p, q):
        
        # compare p and q
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
            
        # then recursively compare p left and q left; p right and q right
        return self.same_tree(p.left, q.left) and \
        self.same_tree(p.right, q.right)
        


solution = Solution()

tree1 = TreeNode("A", TreeNode("B", TreeNode("D"), TreeNode("E")), TreeNode("C"))
tree2 = TreeNode("A", TreeNode("B", TreeNode("D"), TreeNode("E")), TreeNode("C"))

print(solution.same_tree(tree1, tree2))
# True

#   tree1        tree2
#     A            A
#    / \          / \
#   B   C        B   C
#  / \          / \
# D   E        D   E

tree3 = TreeNode("A", TreeNode("B", TreeNode("D"), TreeNode("E")), TreeNode("F"))
print(solution.same_tree(tree1, tree3))
# False

#   tree1        tree3
#     A            A
#    / \          / \
#   B   C        B   F
#  / \          / \
# D   E        D   E


tree4 = TreeNode("A", TreeNode("B", TreeNode("D"), TreeNode("E")), TreeNode("C", None, TreeNode("F")))
print(solution.same_tree(tree1, tree4))
# False

#   tree1        tree4
#     A            A
#    / \          / \
#   B   C        B   C
#  / \          / \   \
# D   E        D   E   F
