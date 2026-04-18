class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        mp = {}
        

        for i,n in enumerate(nums):
            if n in mp:
                mp[n].append(i)
            else:
                mp[n] = [i]
        
        seen = set()

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                residual = 0 - (nums[i] + nums[j])
                if residual in mp.keys():
                    idxs: list = mp[residual]
                    for k in idxs:
                        if k > j:
                            trip = tuple(sorted((nums[i], nums[j], nums[k])))
                            if trip not in seen:
                                seen.add(trip)
                                res.append(trip)

        return res



                    