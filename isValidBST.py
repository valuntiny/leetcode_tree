# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root, largerThan = float('-inf'), lessThan = float('inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        if root.val >= lessThan or root.val <= largerThan:
            return False

        return self.isValidBST(root.left, largerThan, min(lessThan, root.val)) and self.isValidBST(root.right, max(largerThan, root.val), lessThan)
