# Merge Alternately - Difficulty Level: Easy

## Problem Statement

You are given two strings `word1` and `word2`. Merge the strings by adding letters in alternating order, starting with `word1`. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

### Example 1:

Input: `word1 = "abc", word2 = "pqr"`  
Output: `"apbqcr"`

### Example 2:

Input: `word1 = "ab", word2 = "pqrs"`  
Output: `"apbqrs"`

### Example 3:

Input: `word1 = "abcd", word2 = "pq"`  
Output: `"apbqcd"`


## Intuition

The problem requires alternating the characters from both strings, starting with the first string. This can be done by iterating through both strings and adding characters to the result. If one string is longer, we can append the remaining characters after the loop.

## Approach

1. **Iterate through both strings** using a for loop with the range equal to the length of the longer string.
2. **Alternately append characters** from both strings to the result list.
3. After iterating through both strings, if one string is longer, append the remaining characters to the result.
4. **Return the merged string** using `''.join()` to convert the list back to a string.


## Time and Space Complexity

#### Time Complexity
The time complexity of the solution is **O(max(n, m))**, where `n` and `m` are the lengths of `word1` and `word2`, respectively.

- The `for` loop iterates over the maximum length of the two strings, ensuring that we process all characters from both strings, even if one is shorter than the other.
- The appending operation inside the loop is **O(1)**, meaning that each character from both `word1` and `word2` is processed in constant time.
- The `.join()` operation at the end also takes **O(n + m)** time, where `n` and `m` are the lengths of the strings, as it joins all characters into a single string.

Thus, the overall time complexity is **O(max(n, m))**, dominated by the iteration and joining operations.

#### Space Complexity
The space complexity of the solution is **O(n + m)**.

- We use an auxiliary list `result` to store the merged characters from both strings. In the worst case, the list will hold all the characters from both `word1` and `word2`, resulting in a space usage of **O(n + m)**.
- The `.join()` operation, which is **O(n + m)**, does not affect the overall space complexity since it's used to convert the list back to a string.

Thus, the space complexity is **O(n + m)** due to the storage requirements for the result list.
