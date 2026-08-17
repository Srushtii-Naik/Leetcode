'''
Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "IceCreAm"
Output: "AceCreIm"
Explanation:
The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:
Input: s = "leetcode"
Output: "leotcede"

Constraints:
1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s = list(s)  # convert string to list for in-place modification
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] not in vowels:
                left += 1
                continue
            if s[right] not in vowels:
                right -= 1
                continue

            # Swap vowels
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return "".join(s)



'''
#include <iostream>
#include <string>
#include <unordered_set>
using namespace std;

class Solution {
public:
    string reverseVowels(string s) {
        unordered_set<char> vowels = {'a','e','i','o','u','A','E','I','O','U'};
        int left = 0, right = s.size() - 1;

        while (left < right) {
            if (vowels.find(s[left]) == vowels.end()) {
                left++;
                continue;
            }
            if (vowels.find(s[right]) == vowels.end()) {
                right--;
                continue;
            }
            // Swap vowels
            swap(s[left], s[right]);
            left++;
            right--;
        }
        return s;
    }
};

int main() {
    Solution sol;
    cout << sol.reverseVowels("IceCreAm") << endl;   // Output: AceCreIm
    cout << sol.reverseVowels("leetcode") << endl;   // Output: leotcede
    return 0;
}

'''