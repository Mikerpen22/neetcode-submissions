class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = {}

        for i, n1 in enumerate(numbers):
            n2 = target - n1

            # if seen the difference before
            if n2 in mp:
                return [mp[n2]+1, i+1]

            mp[n1] = i
        return []


