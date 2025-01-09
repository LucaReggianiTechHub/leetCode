class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = [ch for ch in s if ch in "aeiouAEIOU"]
        result = []
        
        for char in s:
            if char in "aeiouAEIOU":
                result.append(vowels.pop())  # pop from the end of the vowels list
            else:
                result.append(char)
        
        return "".join(result)
