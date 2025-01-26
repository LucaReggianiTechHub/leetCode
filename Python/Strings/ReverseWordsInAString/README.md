# Reverse Words in a String - Difficulty Level: Medium

## Problem Statement

Given an input string `s`, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in `s` will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that `s` may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

### Example 1:

Input:  
`s = "the sky is blue"`  
Output:  
`"blue is sky the"`

### Example 2:

Input:  
`s = "  hello world  "`  
Output:  
`"world hello"`  
Explanation: Your reversed string should not contain leading or trailing spaces.

### Example 3:

Input:  
`s = "a good   example"`  
Output:  
`"example good a"`  
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

---

## Intuition

The problem requires reversing the order of words in a string while ensuring the output string is clean:
- Leading, trailing, and extra spaces between words should be removed.
- Words should be separated by a single space.

We can split the string into words, reverse the order of the words, and join them back together with a single space.

---

## Approach

1. **Split the String**:
   - Use `s.split()` to split the string into a list of words. This automatically removes extra spaces.
2. **Reverse the List**:
   - Reverse the list of words using slicing `[::-1]`.
3. **Join the Words**:
   - Use `" ".join()` to concatenate the words back into a single string with a single space separating them.

## Complexity

### Time Complexity
The time complexity of the solution is **O(n)**, where `n` is the length of the input string `s`.

1. **Splitting the string**:
   - The `s.split()` method splits the string into words, removing extra spaces, and takes **O(n)** time because it iterates through the entire string.
   
2. **Reversing the list**:
   - Reversing the list of words using slicing (`[::-1]`) takes **O(k)**, where `k` is the number of words. In the worst case, `k` is proportional to `n`.

3. **Joining the words**:
   - The `" ".join()` operation combines the words into a single string, which also takes **O(n)** time.

Since these steps are performed sequentially, the overall time complexity is **O(n)**.

### Space Complexity
The space complexity of the solution is **O(n)**.

- The `split()` operation creates a list of words, which requires **O(n)** space.
- The `join()` operation produces a new string, which also takes **O(n)** space.

Thus, the total space complexity is **O(n)** due to the storage requirements of the intermediate list of words and the resulting string.

