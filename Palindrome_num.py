'''
Palindrome Number
Given an integer x, return true if x is a palindrome, and false otherwise.

 
Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 
Constraints: -231 <= x <= 231 - 1

Follow up: Could you solve it without converting the integer to a string?

'''

def isPalindrome(x):
    if x < 0:
        return False
    original = x
    reverse_num = 0
    while x > 0:
        last_digit = x % 10
        reverse_num = reverse_num * 10 + last_digit
        x = x // 10
    return original == reverse_num

print(isPalindrome(121))   # True
print(isPalindrome(-121))  # False
print(isPalindrome(10))    # False

# ___________________________________________________________________________________________________________________________________________________________________________________


def isPalindrome(x):
    # EXPLANATION: If number is negative, it can NEVER be a palindrome
    # Because negative sign (-) only appears at the front
    # When reversed, the minus sign would be at the end, so it's different
    # Example: -121 reversed would be 121- (not same)
    if x < 0:
        return False
    
    # EXPLANATION: Store original number in a variable
    # We need this to compare at the end
    original = x
    
    # EXPLANATION: This variable will store the reversed number
    # Start with 0 and build it digit by digit
    reversed_num = 0
    
    # EXPLANATION: Keep looping until x becomes 0
    # We will remove last digit one by one
    while x > 0:
        
        # EXPLANATION: Get the LAST digit of current number
        # % is modulo operator - it gives remainder when divided by 10
        # Example: 121 % 10 = 1 (last digit)
        # Example: 12 % 10 = 2 (last digit)
        last_digit = x % 10
        
        # EXPLANATION: Add this digit to reversed number
        # First multiply existing reversed_num by 10 to shift left
        # Then add the last_digit
        # Example: reversed_num=0, last_digit=1 → 0*10+1 = 1
        # Example: reversed_num=12, last_digit=3 → 12*10+3 = 123
        reversed_num = reversed_num * 10 + last_digit
        
        # EXPLANATION: Remove the last digit from original number
        # // is integer division - it divides and rounds down
        # Example: 121 // 10 = 12 (removed last digit 1)
        # Example: 12 // 10 = 1 (removed last digit 2)
        x = x // 10
    
    # EXPLANATION: Compare original number with reversed number
    # If they are same, it's a palindrome
    # Example: original=121, reversed=121 → True
    # Example: original=123, reversed=321 → False
    return original == reversed_num