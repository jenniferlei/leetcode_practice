# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:

# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def DFS(node):
            if not node: # if there is no node, it is a height of 0 and balanced
                return (True, 0)

            left = DFS(node.left) # bubble down to lowest left node, get tuple (balanced, height)
            right = DFS(node.right)

            balanced = left[0] and right[0] and abs(left - right) <= 1

            return (balanced, 1 + max(left, right))

        return DFS(root)[0]



class BinaryNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        
    def is_balanced(self):
        """Is the tree at this node balanced?"""

        # START SOLUTION

        def _num_descendants(node):
            """Returns number of descendants or None if already imbalanced."""

            if not node:
                # Our base case: we're not a real node (child of a leaf)
                return 0

            # Get descendants on left; if "None", already imbalanced---bail out
            left = _num_descendants(node.left)

            if left is None:
                return None

            # Get descendants on right; if "None", already imbalanced---bail out
            right = _num_descendants(node.right)

            if right is None:
                return None

            if abs(left - right) > 1:
                # Heights vary by more than 1 -- imbalanced!
                return None

            # Height of this node is height of our deepest descendant + ourselves
            return max(left, right) + 1

        return _num_descendants(self) is not None
        
tree = BinaryNode("A", BinaryNode("B", BinaryNode("D", BinaryNode("F")), BinaryNode("E")), BinaryNode("C"))
print(tree.is_balanced())
# False


#       A
#      / \
#     B   C
#    / \
#   D   E
#  /
# F















# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:

# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# recursive
# check height of left and right node
# if height difference > 1, return False
# else return True

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# class Solution:
#     def balanced_binary_tree(self, root):

#         def DFS(root):
#             if not root:
#                 return [True, 0]
    
#             # recursively go down to the lowest nodes to get height of node
#             left = DFS(root.left) # get height of left node
#             right = DFS(root.right) # get height of right node
#             balanced = (left[0] and right[0] and abs(left[1] - right[1] <= 1)
                
#             return [balanced, max(left, right) + 1]
#             # returns nodes max height (either left or right height)
    
#         return DFS(root)[0] # go through each node recursively