'''
 Number of Segments in a String

Given a string s, return the number of segments in the string.
A segment is defined to be a contiguous sequence of non-space characters.

Example 1:
Input: s = "Hello, my name is John"
Output: 5
Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]

Example 2:
Input: s = "Hello"
Output: 1
 
Constraints:
0 <= s.length <= 300
s consists of lowercase and uppercase English letters, digits, or one of the following characters "!@#$%^&*()_+-=',.:".
The only space character in s is ' '.
'''

class Solution:
    def countSegments(self, s: str) -> int:
        segments = 0
        for i in range(len(s)):
            if s[i] != ' ' and (i==0 or s[i-1] == ' '):
                segments = segments + 1
        return segments 


# ______________________________________________________________________________________________________________________________________________________________________________



class Solution:
    def countSegments(self, s: str) -> int:
        # EXPLANATION: Initialize counter to 0
        # This will count how many segments (words) we find
        segments = 0
        
        # EXPLANATION: Loop through each character in the string
        # We'll check each character to find where segments start
        for i in range(len(s)):
            
            # EXPLANATION: Check if current character starts a new segment
            # A segment starts when:
            # 1. Current character is NOT a space
            # 2. AND (we are at first character OR previous character was a space)
            # Example: "Hello, my name is John"
            # At i=0: 'H' not space, i==0 → start new segment
            # At i=6: ' ' skip
            # At i=7: 'm' not space, previous char at i=6 is space → start new segment
            if s[i] != ' ' and (i == 0 or s[i-1] == ' '):
                # EXPLANATION: Increment segment counter
                segments = segments + 1
        
        # EXPLANATION: Return total number of segments found
        return segments