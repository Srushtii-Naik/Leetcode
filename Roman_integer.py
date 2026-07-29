'''
Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 
Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 
Constraints: 1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
'''


class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        total =0

        for i, char in enumerate(s):
            current_val = values[char]
            if i < len(s)-1:
                next_val = values[s[i+1]]
                if current_val < next_val:
                    total = total - current_val
                else:
                    total = total + current_val
            else:
                    total = total + current_val
        return total 

sol = Solution()
print(sol.romanToInt("III"))      # Output: 3
print(sol.romanToInt("LVIII"))    # Output: 58
print(sol.romanToInt("MCMXCIV"))  # Output: 1994



# ___________________________________________________________________________________________________________________________________________________________________________________
def romanToInt(s):
    # EXPLANATION: Create a dictionary that maps each Roman symbol to its value
    # This is like a lookup table - when we see 'I', we know it's 1
    # When we see 'V', we know it's 5, and so on
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    # EXPLANATION: This variable will store our final answer
    # Start with 0 and keep adding values as we go through the string
    total = 0
    
    # EXPLANATION: Loop through each character in the string
    # 'i' is the index position (0, 1, 2, 3...)
    # 'char' is the actual Roman character at that position
    for i, char in enumerate(s):
        
        # EXPLANATION: Get the value of current Roman character
        # Example: if char is 'X', current_value = 10
        current_value = roman_values[char]
        
        # EXPLANATION: Check if we are NOT at the last character
        # If we are at last character, there's no next character to compare with
        if i < len(s) - 1:
            
            # EXPLANATION: Get the value of the NEXT character
            # Example: in "IV", if current is 'I', next is 'V'
            # next_value = 5
            next_value = roman_values[s[i + 1]]
            
            # EXPLANATION: This is the IMPORTANT rule for Roman numerals
            # If current value is LESS than next value, we need to SUBTRACT
            # Example: "IV" → I(1) < V(5) → subtract: 5 - 1 = 4
            # Example: "IX" → I(1) < X(10) → subtract: 10 - 1 = 9
            # Example: "CM" → C(100) < M(1000) → subtract: 1000 - 100 = 900
            if current_value < next_value:
                # EXPLANATION: Subtract current value from total
                # We subtract now, and later when we see the next character,
                # we will add its full value
                # Example: "IV" → total = -1 (for I), next loop V adds 5 → total = 4
                total = total - current_value
            else:
                # EXPLANATION: Current value is greater or equal to next
                # So we just add it normally
                # Example: "VI" → V(5) > I(1) → add: 5 + 1 = 6
                # Example: "II" → I(1) = I(1) → add: 1 + 1 = 2
                total = total + current_value
        else:
            # EXPLANATION: This is the LAST character of the string
            # No next character to compare with, so just add its value
            # Example: "III" → last character is 'I', add 1 → total = 3
            total = total + current_value
    
    # EXPLANATION: Return the final calculated total
    return total
