class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        min_len = min([len(s) for s in strs])

        for i in range(min_len):
            current_round_char = set([s[i] for s in strs])
            if len(current_round_char) == 1:
                # match
                res += strs[0][i]
            else:
                return res
        return res
        


        