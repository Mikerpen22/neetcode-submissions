class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        timeToTarget = [(target - position[i])/speed[i] for i in range(len(position))]
        state = list(zip(position, speed, timeToTarget))

        # 根據離終點位置排
        state.sort(key=lambda x: x[0], reverse=True)

        bottleneck = 0
        cluster = 0
        for i, current_state in enumerate(state):
            p, s, t = current_state
            # 如果我需要到終點的時間 比 目前的bottoleneck還快，還是沒用，因為我位置在他後面
            # 比 目前的bottoleneck還慢 -> 我自己變成新的bottleneck -> cluster += 1
            if t > bottleneck:
                bottleneck = t
                cluster += 1

        return cluster





