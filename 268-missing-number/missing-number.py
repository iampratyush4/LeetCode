class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        S=(n*(n+1))//2
        print(S)
        nums_sum=sum(nums)
        return (S - nums_sum)
        






        