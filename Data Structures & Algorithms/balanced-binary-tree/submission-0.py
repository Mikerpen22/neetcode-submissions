# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def getHeight(root) -> int:
            if not root:
                return 0
            return 1 + max(getHeight(root.left), getHeight(root.right))
        # bottom up 的話就不用brute force 的o(n^2)
        if not root:
            return True
        leftH = getHeight(root.left)
        rightH = getHeight(root.right)

        if abs(leftH-rightH) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False


        
        
        