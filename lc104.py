# LeetCode 104 
# Max Depth 
# Depth First Search : Recursive Solution
# Time Complexity: O(n) , where n = number of nodes
# Space Complexity: O(n), where n = number of nodes

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        