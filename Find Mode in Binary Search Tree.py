# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        def inorder_traversal(node):
            nonlocal prev, max_count, current_count

            if not node:
                return

            inorder_traversal(node.left)

            if prev is None:
                current_count = 1
            elif node.val == prev:
                current_count += 1
            else:
                current_count = 1

            if current_count > max_count:
                max_count = current_count
                modes.clear()
                modes.append(node.val)
            elif current_count == max_count:
                modes.append(node.val)

            prev = node.val

            inorder_traversal(node.right)

        modes = []
        prev = None
        max_count = 0
        current_count = 0

        inorder_traversal(root)

        return modes
