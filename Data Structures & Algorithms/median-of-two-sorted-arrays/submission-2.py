from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 1. 永遠對「較短」的陣列做二分搜尋
        # 目的：降低時間複雜度至 O(log(min(m, n)))，且確保二分搜尋時 j 不會算出負太多的非法索引
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        total = len(nums1) + len(nums2)
        half = total // 2  # 左半邊預計要放的總元素量

        # 搜尋範圍是 nums1 的「索引」
        l, r = 0, len(nums1) - 1

        while True:  # 題目保證有解，一定會 return 出去
            # i 代表 nums1 左半邊最後一個元素的索引
            i = l + (r - l) // 2 
            
            # j 代表 nums2 左半邊最後一個元素的索引
            # 計算由來：(i + 1) + (j + 1) = half  =>  j = half - i - 2
            j = half - i - 2  

            # -------------------------------------------------------------
            # 邊界哨兵處理 (Boundary Handling)
            # 若索引越界，用 -inf 或 inf 填補，避免 IndexError 且保持邏輯一致
            # -------------------------------------------------------------
            ALeft  = nums1[i]       if i >= 0             else float("-inf")
            ARight = nums1[i + 1]   if (i + 1) < len(nums1) else float("inf")
            
            BLeft  = nums2[j]       if j >= 0             else float("-inf")
            BRight = nums2[j + 1]   if (j + 1) < len(nums2) else float("inf")

            # -------------------------------------------------------------
            # 檢查是否完成正確切分 (Valid Partition)
            # 條件：左邊最大值 <= 右邊最小值 (交叉檢查)
            # -------------------------------------------------------------
            if ALeft <= BRight and BLeft <= ARight:
                # 奇數狀況：中位數是右半邊的最小值 (因為 half 用 //2 取整，右半邊多 1 個元素)
                if total % 2:
                    return min(ARight, BRight)
                # 偶數狀況：左半邊最大值與右半邊最小值的平均數
                else:
                    return (max(ALeft, BLeft) + min(ARight, BRight)) / 2
            
            # -------------------------------------------------------------
            # 調整二分搜尋範圍
            # -------------------------------------------------------------
            elif ALeft > BRight:
                # A 拿太多/太大了，切口需要往左移
                r = i - 1
            else:
                # B 拿太多/太大了 (即 BLeft > ARight)，切口需要往右移 (A 要多拿一點)
                l = i + 1