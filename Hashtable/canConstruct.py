'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false
'''
def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    if len(ransomNote) > len(magazine):
        return False
    
    ch_count = {}
    for ch in magazine:
        ch_count[ch] = ch_count.get(ch, 0) + 1
    
    for ch in ransomNote:
        if ch not in ch_count or ch_count[ch] == 0:
            return False
        ch_count[ch] -= 1
    return True
