
#Duplicates allowed. Min Max solution

class Solution(object):
    def isValidBST(self, root):
        return self.check_bst(root, None, None)

    def check_bst(self,node, min, max):
        if not node:
            return True
        if (max is not None and node.val >= max) or (min is not None and node.val <= min):
            return False
        return self.check_bst(node.left, min, node.val) and self.check_bst(node.right, node.val, max)


# Solution if there are no duplicates in the tree

# class Solution(object):
#     inorder = []
#     def isValidBST(self, root):
#         if not root:
#             return True
#         if not root.left and not root.right:
#             return True
#
#         self.dfs(root)
#         if self.is_sorted(self.inorder):
#             return True
#         else:
#             return False
#
#     def dfs(self, root):
#         if root:
#             self.dfs(root.left)
#             self.inorder.append(root.val)
#             self.dfs(root.right)
#
#
#     def is_sorted(self, inorder):
#         for i in range(0, len(inorder)-1):
#             if inorder[i] > inorder[i+1]:
#                 return False
#         return True
