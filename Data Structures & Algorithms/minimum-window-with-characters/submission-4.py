class Solution:

    def minWindow(self, s: str, t: str) -> str:
        # basic edge case
        if t == "":
            return ""

        # 【核心帳本】：紀錄目標 t 中，每個字元「總共需要多少個」
        countT = {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1

        # 【當前窗口】：紀錄目前滑動窗口內，各字元的累積數量
        window = {}

        # 【達標計數器】：
        # have: 目前窗口內，已經有多少個「獨特字元」達到了 countT 的數量要求
        # need: 目標 t 裡面，總共有多少個「獨特字元」需要被滿足
        have:int = 0
        need:int = len(countT)

        # 紀錄最終答案的區間指針 [start, end] 與目前找到的最短長度
        res = [-1, -1]
        resLen = float("inf")

        # 初始化左指針，開始讓右指針向右「擴張」
        l = 0
        for r in range(len(s)):
            c = s[r]
            # 1. 吞入字元：將右指針指向的字元納入當前窗口
            window[c] = window.get(c, 0) + 1

            # 2. 檢查達標：如果這個字元是我們需要的，且數量「剛好滿足」目標需求，達標種類 +1
            # (用 == 可以避免重複計算超過需求的字元)
            if c in countT and window[c] == countT[c]:
                have += 1

            # 3. 收縮窗口：當所有需要的字元都滿足了 (have == need)，嘗試將左指針向右縮，尋找更短的可能
            while have == need:
                # 發現更短的有效窗口，立刻更新歷史最佳解
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # 吐出字元：準備將左指針指向的字元移出窗口
                left_char = s[l]
                window[left_char] -= 1

                # 4. 檢查破產：如果被移出的字元是目標需要的，且移出後「低於」目標需求數量，達標種類 -1
                if (
                    left_char in countT
                    and window[left_char] < countT[left_char]
                ):
                    have -= 1

                # 左指針右移，繼續嘗試收縮
                l += 1

        # 根據最終紀錄的座標切片返回答案，若 resLen 沒變過代表無解
        l, r = res
        return "" if resLen == float("inf") else s[l : r + 1]