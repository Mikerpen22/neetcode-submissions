class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # zip the two lists which make things easier
        # sort by pos
        # target = 10
        # [(7, 1, 3), (4, 2, 3), (1, 2, 4.5), (0, 1, 10)]
        n = len(position)
        ideal_time_to_target = [(target - position[i])/speed[i] for i in range(len(speed))]
        state = list(zip(position, speed, ideal_time_to_target))
        state.sort(key=lambda x: x[0], reverse=True)

        cluster = 0
        # 我前面這堆車（我不care有幾台）最多要花多久才到，這是我的bottleneck
        bottleneck = 0
        for i in range(n):
            # 目前我比choke time慢，我至少確定我會成為一個cluster
            # 如果我比choke time塊也沒用，因為被bottleneck卡住了
            if state[i][2] > bottleneck:
                cluster += 1
                bottleneck = state[i][2]
            
            
        return cluster




            



    





        



