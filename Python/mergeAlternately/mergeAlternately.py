class Solution:
    def mergeAlternately(self, word1, word2):
        # Initialize an empty list to store the merged result.
        result = []
        # Iterate over the maximum length of the two strings
        for i in range(max(len(word1), len(word2))):
            # Append character from word1 if we haven't exhausted it
            if i < len(word1):
                result.append(word1[i])
            
            # Append character from word2 if we haven't exhausted it
            if i < len(word2):
                result.append(word2[i])
        
        # Convert the list of characters into a string and return it.
        return ''.join(result)
