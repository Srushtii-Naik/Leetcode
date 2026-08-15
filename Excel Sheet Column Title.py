'''
Excel Sheet Column Title

Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:
Input: columnNumber = 1
Output: "A"

Example 2:
Input: columnNumber = 28
Output: "AB"

Example 3:
Input: columnNumber = 701
Output: "ZY"
'''

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # EXPLANATION: Create empty string to store the result
        # We'll build the title from right to left
        # Example: 28 → "AB" (we build "B" then "A")
        result = ""
        
        # EXPLANATION: Keep looping until columnNumber becomes 0
        # We'll convert the number to letters one by one
        while columnNumber > 0:
            
            # EXPLANATION: Adjust for 1-indexed system
            # Excel columns are 1-indexed (A=1, B=2, ..., Z=26)
            # But we need 0-indexed for calculation (A=0, B=1, ..., Z=25)
            # So we subtract 1 from columnNumber
            # Example: columnNumber=28 → 28-1=27
            columnNumber = columnNumber - 1
            
            # EXPLANATION: Get the remainder when divided by 26
            # This gives us the position of the current letter (0-25)
            # Example: 27 % 26 = 1 → index 1 = 'B'
            remainder = columnNumber % 26
            
            # EXPLANATION: Convert number to letter
            # ord('A') = 65, so 65 + 0 = 'A', 65 + 1 = 'B', etc.
            # Example: remainder=1 → chr(65+1) = 'B'
            letter = chr(ord('A') + remainder)
            
            # EXPLANATION: Add letter to the FRONT of result
            # We're building from right to left, so new letter goes at beginning
            # Example: first iteration "B", second iteration "A" + "B" = "AB"
            result = letter + result
            
            # EXPLANATION: Remove the last digit we just processed
            # Integer division by 26 gives us the remaining part
            # Example: 27 // 26 = 1 → next iteration processes 1
            columnNumber = columnNumber // 26
        
        # EXPLANATION: Return the final column title
        return result

    