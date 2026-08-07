'''
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.
Return the quotient after dividing dividend by divisor.
Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.

Example 2:
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.
 

Constraints:
-231 <= dividend, divisor <= 231 - 1
divisor != 0

'''
# ___________________________________________________________________________________________________________________________________________________________________________________


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # EXPLANATION: Handle special case where result overflows 32-bit integer
        # If dividend is -2^31 and divisor is -1, result would be 2^31
        # But max positive is 2^31 - 1, so return max positive
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        # EXPLANATION: Determine if result will be negative
        # If signs are different (one positive, one negative), result is negative
        # Example: 10 and -3 → negative, -10 and 3 → negative
        # Example: 10 and 3 → positive, -10 and -3 → positive
        negative = (dividend < 0) != (divisor < 0)
        
        # EXPLANATION: Work with positive numbers to make subtraction easier
        # Use abs() to get absolute value of both numbers
        # Example: -10 becomes 10, -3 becomes 3
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        # EXPLANATION: Initialize quotient to 0
        # We'll count how many times divisor fits into dividend
        quotient = 0
        
        # EXPLANATION: Keep subtracting divisor from dividend while dividend >= divisor
        # This is like repeated subtraction
        # Example: 10 ÷ 3
        # 10 >= 3 → subtract → 7, quotient=1
        # 7 >= 3 → subtract → 4, quotient=2
        # 4 >= 3 → subtract → 1, quotient=3
        # 1 >= 3 → false, stop
        while dividend >= divisor:
            # EXPLANATION: Subtract divisor from dividend
            dividend = dividend - divisor
            # EXPLANATION: Increment quotient by 1
            quotient = quotient + 1
        
        # EXPLANATION: Apply the negative sign if needed
        # If negative is True, make quotient negative
        if negative:
            quotient = -quotient
        
        # EXPLANATION: Return the final quotient
        return quotient


# ___________________________________________________________________________________________________________________________________________________________________________________

'''
dividend = 10, divisor = 3
Step 1: Check overflow? No (10 is not min_int)
Step 2: Determine sign: (10<0) != (3<0) → False != False → False (positive)
Step 3: Use absolute values: dividend=10, divisor=3
Step 4: Repeated subtraction:
  dividend=10, divisor=3
  Loop 1: 10 >= 3 → dividend=7, quotient=1
  Loop 2: 7 >= 3 → dividend=4, quotient=2
  Loop 3: 4 >= 3 → dividend=1, quotient=3
  Loop 4: 1 >= 3 → false, stop
Step 5: Apply sign: negative=False, so quotient=3
Return: 3

'''


# ___________________________________________________________________________________________________________________________________________________________________________________

'''
dividend = 7, divisor = -3
Step 1: Check overflow? No (7 is not min_int)
Step 2: Determine sign: (7<0) != (-3<0) → False != True → True (negative)
Step 3: Use absolute values: dividend=7, divisor=3
Step 4: Repeated subtraction:
  dividend=7, divisor=3
  Loop 1: 7 >= 3 → dividend=4, quotient=1
  Loop 2: 4 >= 3 → dividend=1, quotient=2
  Loop 3: 1 >= 3 → false, stop
Step 5: Apply sign: negative=True, so quotient=-2
Return: -2
'''