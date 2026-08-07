# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        【直覺心法：後序測高，順便算直徑】
        1. 核心定義拆解 (First Principles)：
           - 節點「高度 (Height)」：從該節點往下走到最深葉子的「邊數 (edges)」。
           - 穿過該節點的「最長路徑」：左子樹高度 + 右子樹高度。
        2. 為什麼用 DFS (後序遍歷 Post-Order)？
           - 由下而上 (Bottom-Up) 回傳資訊。必須先知道左右子樹的高度，才能算自己的高度與當前的直徑。
        3. 複雜度：
           - 時間：O(N) (每個節點只走一次)
           - 空間：O(H) (遞迴 call stack 深度 = 樹高 H，最壞 O(N))
        """
        res = 0  # 紀錄全域找到的最大直徑 (Global Maximum)

        def dfs(root):
            nonlocal res

            # Base Case：空節點的高度為 0 (向下到底)
            if not root:
                return 0
            
            # 1. 遞迴詢問左右子樹：「你們最深有多高？」(Bottom-Up 訊息傳遞)
            left = dfs(root.left)    # 左子樹高度
            right = dfs(root.right)  # 右子樹高度
            
            # 2. 【核心卡點/考點】以目前節點為拱頂 (V字形彎道) 的最長路徑
            # 左臂長 + 右臂長 = 穿過當前 root 的路徑長度
            res = max(res, left + right)

            # 3. 回傳給上一層父節點：「包含我自己在內，我這條支線最深有多高？」
            # 挑長的走，並加上自己這一條邊 (+1)
            return 1 + max(left, right)

        dfs(root)
        return res