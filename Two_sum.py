'''
You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.


Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:
    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

'''



def two_num(nums, target):
    seen = {}
    for i,num in enumerate(nums):
        needed = target -num
        if needed in seen:
            return [seen[needed],i]
    seen[num] = i

# ___________________________________________________________________________________________________________________________________________________________________________________

def twoSum(nums, target):
    # EXPLANATION: Empty dictionary to store numbers we've already seen
    # Key = the number, Value = its index position
    seen = {}

    # EXPLANATION: Loop through every number in the list
    # i = current index (0, 1, 2...), num = actual number at that index
    for i, num in enumerate(nums):
        
        # EXPLANATION: What number do we need to reach the target?
        # If target is 9 and num is 2, we need 7
        needed = target - num
        
        # EXPLANATION: Check if we've already seen this 'needed' number before
        # If yes, we found our pair!
        if needed in seen:
            # EXPLANATION: Return index of the 'needed' number (from dictionary)
            # and current index i
            return [seen[needed], i]
        
        # EXPLANATION: If we didn't find the pair, store current number in dictionary
        # So future numbers can find it as their 'needed' partner
        seen[num] = i
    
    # EXPLANATION: Should never reach here because problem says solution exists
    return []