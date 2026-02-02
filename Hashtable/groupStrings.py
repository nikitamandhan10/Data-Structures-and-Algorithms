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
