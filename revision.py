class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # EXPLANATION: If the list is empty, return empty string
        # Although constraints say at least 1 string, it's good practice
        if not strs:
            return ""
        
        # EXPLANATION: Start with the first string as our initial prefix
        # We'll compare this with all other strings and shorten it as needed
        # Example: strs = ["flower","flow","flight"]
        # prefix = "flower"
        prefix = strs[0]
        
        # EXPLANATION: Loop through all remaining strings in the list
        # Starting from index 1 (second string) to end
        for i in range(1, len(strs)):
            
            # EXPLANATION: While the current string does NOT start with our prefix
            # We keep removing characters from the end of prefix until it matches
            # Example: prefix="flower", current="flow"
            # "flow".startswith("flower") → False
            # Remove last char: prefix="flowe"
            # "flow".startswith("flowe") → False
            # Remove last char: prefix="flow"
            # "flow".startswith("flow") → True (stop)
            while not strs[i].startswith(prefix):
                
                # EXPLANATION: Remove the last character from prefix
                # prefix[:-1] means "take all characters except the last one"
                # Example: "flower" → "flowe" → "flow"
                prefix = prefix[:-1]
                
                # EXPLANATION: If prefix becomes empty, no common prefix exists
                # Return empty string immediately
                if not prefix:
                    return ""
        
        # EXPLANATION: After checking all strings, return the common prefix
        return prefix
