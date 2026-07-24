# did not solve at first attempt


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # only do binary search on the shorter one of the arrays so we have O(log(min(m, n)))
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        total = len(nums1) + len(nums2)
        half = total // 2

        l, r = 0, len(nums1) - 1
        while True:  # median will always exist
            i = l + (r - l) // 2  # mid (i) 用來track目前A陣列的左partition邊界
            j = half - i - 2  # j 用來track目前B陣列的左parition邊界(套用 example 2就能知道-2)

            # 列出邊界上的element，之後比較好做edge condition比較
            ALeft = nums1[i] if i >= 0 else float("-inf")
            ARight = nums1[i + 1] if (i + 1) < len(nums1) else float("inf")
            BLeft = nums2[j] if j >= 0 else float("-inf")  # half-mid-2 可能負的
            BRight = nums2[j + 1] if j + 1 < len(nums2) else float("inf")

            # stop condition:  this is a valid partition
            if ALeft <= BRight and BLeft <= ARight:
                # if odd, take one number; if even take avg
                if total % 2:
                    return min(ARight, BRight)
                else:
                    return (max(ALeft, BLeft) + min(ARight, BRight)) / 2
            # not valid condition -> move binary search pointers
            elif ALeft > BRight:
                # A的左邊partition太大
                r = i - 1

            else:  # (BLeft > ARight)
                # B 的左邊partition太大
                l = i + 1
