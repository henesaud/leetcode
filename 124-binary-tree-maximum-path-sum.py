# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.result = root.val

        def maxWithoutSplit(root):
            if root is None:
                return 0

            maxL = max(0, maxWithoutSplit(root.left))
            maxR = max(0, maxWithoutSplit(root.right))


            #max with split
            self.result = max(self.result, root.val + maxL + maxR)

            return root.val + max(maxL, maxR)

        maxWithoutSplit(root)
        return self.result
