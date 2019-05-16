#using post order

class Solution(object):
    max = float('-inf')
    def maxPathSum(self, root):
        self.post_order(root)
        return self.max

    def post_order(self, root):
        if not root:
            return float('-inf')
        left = self.post_order(root.left)
        right = self.post_order(root.right)
        self.max = max(self.max, root.val, left, right, left + root.val, right + root.val, left + right + root.val)

        return max(root.val + left, root.val + right, root.val)
