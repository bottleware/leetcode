# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # this is a recursive implementation.

    # Space: O(log n) since this is spawning stack frames. The number of stack
    # frames depends on how many times a recursive function is called. In this
    # case, the depth of a binary tree. The height of a binary tree is log(n).
    def invertTree(self, root):
        # We need a base case to end the cascade of recursive calls
        if root is None:
            return


        # At every node we're at, we want to reverse the tree. Simply reassign
        # each left and right children.
        temp = root.left
        root.left = root.right
        root.right = temp

        # After we reversed the nodes, we need to check their children. We
        # already have a function for that, this recursive one we're in :-)
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)

        return root
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
