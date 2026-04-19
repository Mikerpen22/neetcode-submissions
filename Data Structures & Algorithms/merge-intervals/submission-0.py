class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x:x[0]) # sort by left element
        cur_min, cur_max = intervals[0][0], intervals[0][1]
        res.append(intervals[0])

        for i, interval in enumerate(intervals):
            left, right = interval[0], interval[1]
            
            # check if left is within boundary, if so merge is required
            if left <= cur_max:
                # check if right is also within the boundary
                # if yes that means this interval in entirely absorbed -> do nothing
                # if no, update our right hand boundary
                if right <= cur_max:
                    continue
                else:
                    cur_max = right
                    res[-1][1] = right


            # if left is out of bound, merge not required
            # can append safely and update boundary
            if left > cur_max:
                res.append(interval)
                cur_min, cur_max = left, right
        
        return res
                


            