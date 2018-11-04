'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        level = [root]
        ans = []
        while level:
            temp1 = []  # answer for one level
            for node in level:
                temp1.extend([node.val])
            ans.append(temp1)

            temp2 = []  # nodes in each level
            for node in level:
                temp2.extend([node.left, node.right])
            level = [leaf for leaf in temp2 if leaf is not None]

        return ans