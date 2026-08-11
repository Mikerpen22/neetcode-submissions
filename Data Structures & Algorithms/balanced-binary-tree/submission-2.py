class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node) -> tuple[bool, int]:
            if not node:
                return True, 0
            
            left_balanced, left_h = dfs(node.left)
            right_balanced, right_h = dfs(node.right)
            
            # 當前節點是否平衡：左右子樹皆平衡，且高度差 <= 1
            balanced = left_balanced and right_balanced and abs(left_h - right_h) <= 1
            height = max(left_h, right_h) + 1
            
            return balanced, height

        return dfs(root)[0]