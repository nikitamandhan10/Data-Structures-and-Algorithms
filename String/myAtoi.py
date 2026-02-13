'''
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.
The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.

Example 1:
Input: s = "42"
Output: 42
'''

def myAtoi(self, s: str) -> int:
    s = s.strip()
    if not s:
        return 0
    i = 0
    sign = 1
    if s[i] == '-':
        sign = -1
        i += 1
    elif s[i] == '+':
        i += 1
    
    n = 0
    while i < len(s) and s[i].isdigit():
        n = n * 10 + int(s[i])
        i += 1
    
    n = sign * n
    if n < -2 ** 31:
        return -2 ** 31
    elif n > 2**31 - 1:
        return 2**31 - 1
    else:
        return n
