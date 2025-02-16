
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        else:
            return [perm[:i] + [nums[0]] + perm[i:] for perm in self.permute(nums[1:]) for i in range(len(perm) + 1)] 