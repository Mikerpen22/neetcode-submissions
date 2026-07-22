class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            # 1. 幸運中獎
            if nums[mid] == target:
                return mid

            # 2. 判斷哪一半是「單調遞增（完美排序）」
            
            # Case A: 左半邊 (l ~ mid) 是單調遞增
            # 視覺想像: [4, 5, 6, 7, 0, 1, 2] -> nums[l]=4 <= nums[mid]=7，左邊沒斷層
            if nums[l] <= nums[mid]:
                # target 是否精準落在左邊這個「安全區間」？
                if nums[l] <= target < nums[mid]:
                    r = mid - 1  # 往左邊找
                else:
                    l = mid + 1  # 往右邊找（去有斷層的那區）

            # Case B: 右半邊 (mid ~ r) 是單調遞增
            # 視覺想像: [6, 7, 0, 1, 2, 4, 5] -> nums[mid]=1 < nums[r]=5，右邊沒斷層
            else:
                # target 是否精準落在右邊這個「安全區間」？
                if nums[mid] < target <= nums[r]:
                    l = mid + 1  # 往右邊找
                else:
                    r = mid - 1  # 往左邊找（去有斷層的那區）

        return -1