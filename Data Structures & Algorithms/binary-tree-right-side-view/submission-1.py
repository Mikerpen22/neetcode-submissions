# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        cur_level = deque()
        res = []

        # Thoughts: 
        # this depends on level, at the same level, we need to find the right most node
        # seems like a perfect candidate for bfs
        if not root:
            return []
        cur_level.append(root)

        while cur_level:
            level_size = len(cur_level)
            res.append(cur_level[0].val)
            for i in range(level_size):
                node = cur_level.popleft()
                if node.right: 
                    cur_level.append(node.right)
                if node.left:
                    cur_level.append(node.left)

        return res
            



        