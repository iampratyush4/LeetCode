class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        dic={')': '(', '}': '{', ']' : '['}
        for c in s:
            if c in dic:
                if l and l[-1]==dic[c]:
                    l.pop()
                else:
                    return  False
            else:
                l.append(c)
        return  True if not l else False




        