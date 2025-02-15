class Solution:
    def maxSubArray(self, nums: List[int]) -> int:  
        currsum=nums[0]
        sum=0
        for i in nums:
            if sum <0:
                sum=0
            sum =sum +i
            currsum=max(currsum,sum)

        return currsum

        