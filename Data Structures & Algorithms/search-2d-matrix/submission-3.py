class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # treat matrix's first number of each row as the actual number and do binary search
        # after we locate which row it's at, then we do binary search within that row

        m, n = len(matrix), len(matrix[0])

        l_row, r_row = 0, m - 1
        row = -1

        while l_row <= r_row:
            mid = l_row + (r_row - l_row) // 2
            if matrix[mid][-1] < target:
                l_row = mid + 1
            elif matrix[mid][0] > target:
                r_row = mid - 1
            else:
                row = mid
                break
        
        if row == -1:
            return False

        # now do binary search on matrix[row]
        l, r = 0, n - 1
        while l <= r:
            mid = l + (r - l) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return False