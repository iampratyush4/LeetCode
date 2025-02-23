from itertools import permutations
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Sort the list to handle duplicates and for two-pointer approach
        nums.sort()
        quadruplets = []
        
        # Iterate through the list to fix the first element
        for i in range(len(nums) - 3):
            # Skip duplicate elements for the first position
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Iterate for the second element
            for j in range(i + 1, len(nums) - 2):
                # Skip duplicate elements for the second position
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # Use two pointers for the third and fourth elements
                left, right = j + 1, len(nums) - 1
                while left < right:
                    # Calculate the sum of the four numbers
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    # If we find the target, add the quadruplet
                    if current_sum == target:
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Skip duplicate elements for the third and fourth positions
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        
                        # Move both pointers inward
                        left += 1
                        right -= 1
                    
                    # If the current sum is less than the target, move the left pointer to the right
                    elif current_sum < target:
                        left += 1
                    # If the current sum is greater than the target, move the right pointer to the left
                    else:
                        right -= 1
        
        return quadruplets

            