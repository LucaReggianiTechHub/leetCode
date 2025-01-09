# Reverse Vowels of a String - Difficulty Level: Easy

## Problem Statement

Given a string s, reverse only all the vowels in the string, and return the resulting string. The vowels are 'a', 'e', 'i', 'o', and 'u', which can appear in both lower and upper cases, and they may appear multiple times.

### Examples

#### Example 1:
Input:  
s = "IceCreAm"  

Output:  
"AceCreIm"  

Explanation:  
The vowels in "IceCreAm" are ['I', 'e', 'e', 'A']. Reversing them results in ['A', 'e', 'e', 'I']. Substituting them back into their original positions yields "AceCreIm".

#### Example 2:
Input:  
s = "leetcode"  

Output:  
"leotcede"  

Explanation:  
The vowels in "leetcode" are ['e', 'e', 'o', 'e']. Reversing them results in ['e', 'o', 'e', 'e']. Substituting them back gives "leotcede".

---

## Intuition

The key insight for solving this problem is recognizing that we only need to reverse the vowels in place, leaving the consonants and their positions unchanged. By focusing on extracting and then reversing only the vowels, we minimize the operations on the entire string.

1. Identify and extract all vowels.  
2. Reverse the list of extracted vowels.  
3. Re-insert them into the positions formerly occupied by vowels.

---

## Approach

1. **Extract Vowels**  
   - Iterate through the string s, collecting all characters that are vowels ('a', 'e', 'i', 'o', 'u' in either case) into a separate list.

2. **Reverse the Vowels**  
   - After extracting the vowels, reverse this list. This reversed list will contain the vowels in the order we need to re-insert them.

3. **Construct the Result**  
   - Traverse the original string.  
   - Whenever we encounter a consonant, keep it as is.  
   - Whenever we encounter a vowel, pop from the reversed vowels list (which gives us the last vowel in the reversed order) and place it in the result.

4. **Return the Modified String**  
   - Finally, join all characters back into a string and return it.

---

## Complexity

### Time Complexity

- Extracting vowels involves scanning through all characters of the string once, which is O(n).  
- Creating the result by checking each character again is another O(n).  
- Thus, the overall time complexity is O(n), where n is the length of the string.

### Space Complexity

- We store the vowels in an auxiliary list, which could hold up to O(n) characters in the worst case (if all characters were vowels).  
- Constructing the result also uses O(n) space.  
- Therefore, the space complexity is O(n).
