class Solution(object):
    def isBalanced(self, root):
        def helper(root):
            if root is None:
                return 0, True

            left_h, left_bal = helper(root.left)
            right_h, right_bal = helper(root.right)

            height = 1 + max(left_h, right_h)

            if not left_bal or not right_bal:
                return height, False

            if abs(left_h - right_h) > 1:
                return height, False

            return height, True

        return helper(root)[1]
