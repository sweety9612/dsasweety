# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):

        def dfs(node, curSum):
            if not node:
                return 0

            curSum += node.val

            count = 0
            if curSum == targetSum:
                count += 1

            # Continue path downward
            count += dfs(node.left, curSum)
            count += dfs(node.right, curSum)

            return count

        if not root:
            return 0

        # Paths starting from this node
        return (
            dfs(root, 0)
            + self.pathSum(root.left, targetSum)
            + self.pathSum(root.right, targetSum)
        )
