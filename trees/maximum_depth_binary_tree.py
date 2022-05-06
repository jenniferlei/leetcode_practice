# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0



            

        
        























# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth_recursive_DFS(self, root):
        if not root:
            return 0
    
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth_iterative_DFS(self, root):
        # track depth at each depth search
        stack = [[root, 1]]
        max_depth = 0

        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                stack.append([root.left, depth + 1])
                stack.append([root.right, depth + 1])

        return max_depth

    def maxDepth_BFS(self, root):
        max_depth = 0
        
        if not root:
            return max_depth

        q = deque([root])

        while q: # while q has nodes left
            for i in range(len(q)): # for each node in q, remove and add children to q if any
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            max_depth += 1 # after all nodes one level have been removed, add 1 to max depth
        
        return max_depth

# Input: root = [3,9,20,null,null,15,7]
# Output: 3

#         3
#     |        |
#     9        20
#            |    |
#            15   7