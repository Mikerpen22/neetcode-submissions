class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two pointers, adjust right, left bound to fit to target
        n = len(numbers)
        i, j = 0, n-1


        while i < j:
            curSum = numbers[i] + numbers[j]
            if curSum > target:
                # too large, lower right bound
                j -= 1
            elif curSum < target:
                i += 1
            else:
                return [i+1, j+1]
        return [0,0 ]

