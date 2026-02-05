'''
Perform the following shift operations on a string:
Right shift: Replace every letter with the successive letter of the English alphabet, where 'z' is replaced by 'a'. For example, "abc" can be right-shifted to "bcd" or "xyz" can be right-shifted to "yza".
Left shift: Replace every letter with the preceding letter of the English alphabet, where 'a' is replaced by 'z'. For example, "bcd" can be left-shifted to "abc" or "yza" can be left-shifted to "xyz".
We can keep shifting the string in both directions to form an endless shifting sequence.
For example, shift "abc" to form the sequence: ... <-> "abc" <-> "bcd" <-> ... <-> "xyz" <-> "yza" <-> .... <-> "zab" <-> "abc" <-> ...
You are given an array of strings strings, group together all strings[i] that belong to the same shifting sequence. You may return the answer in any order.
Example 1:
Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
'''
from collections import defaultdict
def groupStrings(self, strings):
    group_shifted = defaultdict(list)
    
    for s in strings:
        if len(s) == 1:
            group_shifted[(-1)].append(s)
        else:
            char_diff = []
            for i in range(1,len(s)):
                char_diff.append((ord(s[i]) - ord(s[i - 1])) % 26)
            group_shifted[tuple(char_diff)].append(s)
        
    return list(group_shifted.values())
