class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 邊界條件
        if not root: 
            return False
        
        # 1. 檢查以當前 root 為根的子樹是否與 subRoot 完全相同
        if self.isSameTree(root, subRoot):
            return True
            
        # 2. 若不同，繼續往左、右子樹尋找起點
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)