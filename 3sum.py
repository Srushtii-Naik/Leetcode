'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.


Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:
3 <= nums.length <= 3000
-105 <= nums[i] <= 105

'''


# ___________________________________________________________________________________________________________________________________________________________________________________



class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # EXPLANATION: Sort the array in ascending order
        # Sorting is necessary for two-pointer technique and duplicate handling
        # Example: [0,1,1] → [0,1,1], [-1,0,1,2,-1,-4] → [-4,-1,-1,0,1,2]
        nums.sort()
        
        # EXPLANATION: Create empty list to store our answer triplets
        result = []
        
        # EXPLANATION: Loop through array to pick first element of triplet
        # We stop at len(nums)-2 because we need at least 2 elements after i
        # Example: if nums has 6 elements, i goes 0,1,2,3 (4 positions)
        # At i=4, only 1 element left after it, can't form triplet
        for i in range(len(nums) - 2):
            
            # EXPLANATION: Skip duplicates for the first element
            # If current number equals previous number, we'll get same triplets
            # Example: [-1,-1,0,1] - first -1 will find triplets
            # Second -1 would find same triplets again, so skip it
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # EXPLANATION: Set left pointer at i+1 (next element after i)
            # Set right pointer at last element of array
            left = i + 1
            right = len(nums) - 1
            
            # EXPLANATION: While left pointer hasn't crossed right pointer
            # We keep searching for pairs that sum to -nums[i]
            while left < right:
                
                # EXPLANATION: Calculate sum of three numbers
                # nums[i] is fixed, we're finding two others
                current_sum = nums[i] + nums[left] + nums[right]
                
                # EXPLANATION: If sum equals 0, we found a valid triplet!
                if current_sum == 0:
                    
                    # EXPLANATION: Add this triplet to our result list
                    # [nums[i], nums[left], nums[right]] creates a new list
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # EXPLANATION: Move both pointers to find next combination
                    left = left + 1
                    right = right - 1
                    
                    # EXPLANATION: Skip duplicates for left pointer
                    # If next number is same as current left, we'll get duplicate
                    # Example: [-2,0,0,2,2] - after finding [-2,0,2]
                    # Skip second 0 and second 2 to avoid duplicates
                    while left < right and nums[left] == nums[left - 1]:
                        left = left + 1
                    
                    # EXPLANATION: Skip duplicates for right pointer
                    # If previous number is same as current right, skip it
                    while left < right and nums[right] == nums[right + 1]:
                        right = right - 1
                
                # EXPLANATION: If sum is less than 0, we need larger sum
                # Since array is sorted, moving left pointer right increases sum
                # Example: [-4,-1,0,2] if sum = -3, move left to get bigger
                elif current_sum < 0:
                    left = left + 1
                
                # EXPLANATION: If sum is greater than 0, we need smaller sum
                # Since array is sorted, moving right pointer left decreases sum
                # Example: [-1,0,1,5] if sum = 4, move right to get smaller
                else:
                    right = right - 1
        
        # EXPLANATION: Return all found unique triplets
        return result

    