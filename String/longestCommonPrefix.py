'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
'''

def longestCommonPrefix(self, strs: List[str]) -> str:
    for i in range(len(strs[0])):
        for string in strs[1:]:
            if i == len(string) or string[i] != strs[0][i]:
                return strs[0][:i]
    
    return strs[0]
