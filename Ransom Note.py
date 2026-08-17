'''
Ransom Note

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:
1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.

'''
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)
        
        for char, freq in ransom_count.items():
            if magazine_count[char] < freq:
                return False
        return True

print(Solution().canConstruct("a", "b"))       # False
print(Solution().canConstruct("aa", "ab"))     # False
print(Solution().canConstruct("aa", "aab"))    # True
print(Solution().canConstruct("abc", "cba"))   # True
print(Solution().canConstruct("abc", "ab"))    # False



'''
#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char, int> freq;
        
        // Count frequency of each char in magazine
        for (char c : magazine) {
            freq[c]++;
        }
        
        // Check if ransomNote can be formed
        for (char c : ransomNote) {
            if (freq[c] <= 0) return false; // not enough chars
            freq[c]--; // use one occurrence
        }
        
        return true;
    }
};

int main() {
    Solution sol;
    cout << boolalpha; // print true/false instead of 1/0
    
    cout << sol.canConstruct("a", "b") << endl;      // false
    cout << sol.canConstruct("aa", "ab") << endl;    // false
    cout << sol.canConstruct("aa", "aab") << endl;   // true
    
    return 0;
}

'''
