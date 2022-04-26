# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:

# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# recursive
# check height of left and right node
# if height difference > 1, return False
# else return True

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanced_binary_tree(self, root):

        def DFS(root):
            if not root:
                return [True, 0]
    
            # recursively go down to the lowest nodes to get height of node
            left = DFS(root.left) # get height of left node
            right = DFS(root.right) # get height of right node
            balanced = (left[0] and right[0] and abs(left[1] - right[1] <= 1)
                
    
            return [balanced, max(left, right) + 1] # returns nodes max height (either left or right height)
    
        return DFS(root)[0] # go through each node recursively