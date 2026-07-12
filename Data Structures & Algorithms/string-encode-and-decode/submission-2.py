class Solution:

    def encode(self, strs: List[str]) -> str:
        # assume strings = ["aaaaaaaaaa", "bb", "c"]
        # encoded -> 10_a2_b1_c
        # pattern = <count>_s
        res = ""
        for s in strs:
            n = len(s)
            res = res + (str(n) + '_' + s) 
        return res


    def decode(self, s: str) -> List[str]:
        # receive <count a>_<string a><count b>_<string_b>
        # len of this next string = int(extract till the first '_')
        
        # use i to keep track of current position
        # use j to keep track of count part
        # use k = keep trace of string part
        i, j, k = 0, 0, 0
        res = []
        
        while i < len(s):
            j = i
            count = ''
            while s[j] != '_':
                count += s[j]
                j += 1
            
            # now we see '_'
            # convert 'count' into actual number
            k = j+1
            cnt = int(count)
            
            res.append(s[k: k+cnt])

            i = k+cnt

        return res










        