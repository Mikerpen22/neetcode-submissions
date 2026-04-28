class Solution:

    def search(self, nums: List[int], target: int) -> bool:
        # first thoughts:
        # - if split by pivot, both sides are sorted
        # - if seen from mid point, there must be at least one side that's sorted -> say both not sorted, the original array couldn't have been sorted
        n = len(nums)
        low, high = 0, n-1

        # first determine which sides is sorted
        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                return True

            if nums[low] == nums[mid] and nums[mid] == nums[high]:
                low += 1
                high-=1

            # lhs is sorted
            elif nums[low] <= nums[mid]:
                # check if target is in lhs's range
                if target >= nums[low] and target < nums[mid]:
                    high = mid-1
                else:
                    # lhs is useless, we need to go to rhs then
                    low = mid+1         
            
            # rhs is sorted    
            elif nums[mid] <= nums[high]:    
                # check if target within rhs's range
                if target > nums[mid] and target <= nums[high]:
                    low = mid+1
                else:
                    # not in rhs, go to lhs then
                    high = mid-1


        return False


        






        

        
