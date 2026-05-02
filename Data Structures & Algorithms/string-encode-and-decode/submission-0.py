class Solution:

    def encode(self, strs: List[str]) -> str:
        tmp = ""
        for s in strs:
            n = len(s)
            tmp = tmp + "_" +  (str(n)) + "_" + s
        print(tmp)
        return tmp

    def decode(self, s: str) -> List[str]:
        k = 0
        n = len(s)
        res = []
        
        while k < n:
            if s[k] == "_":
                # next char will indicate how many char to accumulate
                k+=1
                sl = ""
                while not s[k] == "_":
                    sl += s[k]
                    k+=1
                k+=1
                acc = ""
                for _ in range(int(sl)):
                    acc+= s[k]
                    k+=1
                res.append(acc)
            
        return res

