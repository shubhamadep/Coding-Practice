class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []

        zig = True
        queue = []
        queue.append(root)
        result = []

        while len(queue) > 0:
            level_elements = [e.val for e in queue]

            if zig:
                result.append(level_elements)
            else:
                level_elements.reverse()
                result.append(level_elements)

            zig = not zig
            nqueue = []
            for e in queue:
                if e.left:
                    nqueue.append(e.left)
                if e.right:
                    nqueue.append(e.right)
            queue = nqueue

        return result
