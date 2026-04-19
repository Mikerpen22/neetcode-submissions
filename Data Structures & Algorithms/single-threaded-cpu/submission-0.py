from collections import deque
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        # input: tasks = [[5,2],[4,4],[4,1],[2,1],[3,3]]
        # tasks = [[2,1], [3,3], [4,1], [4,4], [5,2]]
        tasks = [(task[0], task[1], i) for i, task in enumerate(tasks)]
        tasks.sort(key = lambda x: x[0]) # sort by enqueue time
        time = 0
        i = 0
        res = []
        processing = [] # minheap
        
        if tasks:
            time = tasks[0][0]
        
        while i < len(tasks) or processing:
            # move eligible tasks to heap
            while i < len(tasks) and tasks[i][0] <= time:
                enqueue_t, process_t, idx = tasks[i]
                heapq.heappush(processing, (process_t, idx, enqueue_t))
                i += 1

            if processing:
                proc_t, idx, enq_t = heapq.heappop(processing)
                time += proc_t
                res.append(idx)
            else:
                # no task is avaialbe at this time, fastforward time

                time = tasks[i][0]

        return res



        

        

            
            

