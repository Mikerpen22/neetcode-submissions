class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n) time with brute force solution, but how to do this without division?
        # Example: [1,2,4,6]

        # A = [1, 1, 2, 8] => A[i] = multiply from 0 up to i-1 
        # B = [48, 24, 6, 1] => B[i] = multiple from i+1 to len(nums)-1

        # ans = A*B

        # Solution:
        # Build A:
        n = len(nums)
        A = [1]
        B = [1]
        running_A = 1
        running_B = 1
        # 要填滿A,B剩餘n-1個位子
        for i in range(1, n):
            running_A *= nums[i-1]
            running_B *= nums[n-i]
            A.append(running_A)
            B.append(running_B)

        print(running_A, running_B)
        
        res = [] 
        for i in range(n):
            res.append(A[i] * B[n-i-1])
        return res


        

            



