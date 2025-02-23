from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Pointer to track position of non-val elements
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Overwrite element in-place
                k += 1  # Increase count of non-val elements

        return k  # Return count of valid elements