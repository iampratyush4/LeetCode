class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0
        cursum=0
        dicti={0:1}

        for n in nums: 
            cursum=n + cursum
            remainder= cursum-k
            res= res+ dicti.get(remainder,0) //1
            dicti[cursum]= 1+ dicti.get(cursum,0)
        return res