'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
Example 1:
Input: s = "aba"
Output: true
'''

def validPalindrome(self, s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            skipL = s[l + 1: r + 1]
            skipR = s[l:r]
            return skipL == skipL[::-1] or skipR == skipR[::-1]
            
        l += 1
        r -= 1
    return True
