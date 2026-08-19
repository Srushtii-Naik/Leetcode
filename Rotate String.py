'''
Rotate String

Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.
For example, if s = "abcde", then it will be "bcdea" after one shift.
 
Example 1:
Input: s = "abcde", goal = "cdeab"
Output: true

Example 2:
Input: s = "abcde", goal = "abced"
Output: false
 
Constraints:
1 <= s.length, goal.length <= 100
s and goal consist of lowercase English letters.
'''


#Method 1: Using in operator (simple & clean)
def rotateString(s: str, goal: str) -> bool:
    return len(s) == len(goal) and goal in (s + s)


#Method 2: Manual rotation check (loop way)
def rotateString(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False
    for i in range(len(s)):
        rotated = s[i:] + s[:i]   # shift left i times
        if rotated == goal:
            return True
    return False



#Method 3: Using collections.deque (rotate efficiently)
from collections import deque
def rotateString(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False
    dq = deque(s)
    for _ in range(len(s)):
        dq.rotate(-1)  # left shift
        if ''.join(dq) == goal:
            return True
    return False

print(rotateString("abcde", "cdeab"))  # True
print(rotateString("abcde", "abced"))  # False







'''
#include <bits/stdc++.h>
using namespace std;

bool rotateString(string s, string goal) {
    if (s.length() != goal.length()) return false;
    string doubled = s + s;   // contains all rotations
    return doubled.find(goal) != string::npos;
}

int main() {
    string s1 = "abcde", goal1 = "cdeab";
    cout << (rotateString(s1, goal1) ? "true" : "false") << endl;  // true

    string s2 = "abcde", goal2 = "abced";
    cout << (rotateString(s2, goal2) ? "true" : "false") << endl;  // false

    return 0;
}

'''

