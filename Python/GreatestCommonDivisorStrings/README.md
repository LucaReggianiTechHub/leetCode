# GCD of Strings - Difficulty Level: Easy

## Problem Statement

For two strings `s` and `t`, we say "t divides s" if and only if `s = t + t + ... + t` (i.e., `t` is concatenated with itself one or more times).

Given two strings `str1` and `str2`, return the largest string `x` such that `x` divides both `str1` and `str2`.

### Examples

#### Example 1:
Input:  
`str1 = "ABCABC", str2 = "ABC"`  
Output:  
`"ABC"`

#### Example 2:
Input:  
`str1 = "ABABAB", str2 = "ABAB"`  
Output:  
`"AB"`

#### Example 3:
Input:  
`str1 = "LEET", str2 = "CODE"`  
Output:  
`""`

---

## Intuition

The problem requires finding the largest common divisor string between two input strings. Observing the examples, we can deduce:
- If the concatenation `str1 + str2` is not equal to `str2 + str1`, there can be no common divisor string.
- The length of the greatest common divisor string must divide both `len(str1)` and `len(str2)`, as it must repeat to form both strings.

By focusing on these two observations, we can efficiently solve the problem without manually checking substrings.

---

## Approach

1. **Verify Concatenation Rule**:
   - If `str1 + str2 != str2 + str1`, return `""` because no common divisor string exists.

2. **Calculate the GCD of String Lengths**:
   - Use the mathematical greatest common divisor (GCD) of the lengths of the two strings to determine the possible length of the divisor string.

3. **Extract the Candidate**:
   - Extract the substring from `str1` up to the GCD length. This is the potential divisor.

4. **Verify the Candidate**:
   - Check if this candidate can generate both `str1` and `str2` by concatenating itself multiple times.

5. **Return the Result**:
   - If the candidate passes the verification, return it. Otherwise, return `""`.

---

## Complexity

### Time Complexity
The time complexity of the solution is **O(n + m)**, where `n` and `m` are the lengths of `str1` and `str2`, respectively.

- Verifying the concatenation rule (`str1 + str2 == str2 + str1`) takes **O(n + m)**.
- Calculating the GCD of the string lengths is done in **O(log(min(n, m)))**.
- Verifying if the candidate divides both strings takes **O(n + m)**.

Thus, the total time complexity is **O(n + m)**.

### Space Complexity
The space complexity is O(gcd(n, m)).

The substring str1[:length] creates a new string of size length, which corresponds to O(gcd(n, m)) space.

Other operations, such as the math.gcd function and temporary variables, use constant space.

Thus, the space complexity is O(gcd(n, m)).

- We only use a few variables (e.g., for the GCD and the candidate substring) and do not allocate extra space proportional to the input size.

---
