from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Helper function to check if string s can be constructed by repeating string t
        def is_divisible(s, t):
            if len(s) % len(t) != 0:
                return False
            return s == t * (len(s) // len(t))
        
        # Calculate the greatest common divisor of the lengths of str1 and str2
        length = gcd(len(str1), len(str2))
        
        # Candidate substring that could be the gcd string
        candidate = str1[:length]
        
        if is_divisible(str1, candidate) and is_divisible(str2, candidate):
            return candidate
        
        return ""
