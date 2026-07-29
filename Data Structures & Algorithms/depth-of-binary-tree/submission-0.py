# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # BFS
        if not root:
            return 0
        
        q = deque([[root]])
        level = 1
        while q:
            curLevel = q.popleft()
            nextLevel = []
            for node in curLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            if len(nextLevel):
                q.append(nextLevel)
                level += 1
        return level
        