# Kids With the Greatest Number of Candies - Difficulty Level: Easy

## Problem Statement

You are given an integer array `candies`, where each `candies[i]` represents the number of candies the ith kid has, and an integer `extraCandies`, denoting the number of extra candies you can give to any kid. 

Return a boolean array `result` of length `n`, where `result[i]` is `true` if, after giving the ith kid all the extra candies, they will have the greatest number of candies among all the kids, or `false` otherwise.

Note that multiple kids can have the greatest number of candies.

### Examples

#### Example 1:
Input:  
`candies = [2,3,5,1,3], extraCandies = 3`  
Output:  
`[true,true,true,false,true]`  
Explanation:  
- Kid 1 will have 2 + 3 = 5 candies, which is the greatest among the kids.  
- Kid 2 will have 3 + 3 = 6 candies, which is the greatest among the kids.  
- Kid 3 will have 5 + 3 = 8 candies, which is the greatest among the kids.  
- Kid 4 will have 1 + 3 = 4 candies, which is not the greatest among the kids.  
- Kid 5 will have 3 + 3 = 6 candies, which is the greatest among the kids.

#### Example 2:
Input:  
`candies = [4,2,1,1,2], extraCandies = 1`  
Output:  
`[true,false,false,false,false]`  
Explanation:  
There is only 1 extra candy. Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.

#### Example 3:
Input:  
`candies = [12,1,12], extraCandies = 10`  
Output:  
`[true,false,true]`

---

## Intuition

The problem requires checking, for each kid, if they can have the greatest number of candies after receiving all the extra candies. This boils down to comparing the total number of candies of each kid after the extra candies are added to the maximum number of candies that any kid has.

### Observations:
1. The kid with the highest number of candies without the extra ones will be the reference.
2. For each kid, check if their total candies (including the extra ones) are greater than or equal to the maximum number of candies.

---

## Approach

1. **Find the Maximum Candies**:  
   Calculate the maximum number of candies any kid currently has.

2. **Check for Each Kid**:  
   For each kid, add the `extraCandies` to their current number of candies. If this number is greater than or equal to the maximum candies, append `True` to the result list. Otherwise, append `False`.

3. **Return the Result**:  
   Return the final list that contains `True` or `False` for each kid based on whether they have the greatest number of candies after receiving the extra ones.

---
## Complexity

### Time Complexity

The time complexity of the solution is **O(n)**, where `n` is the number of kids (or the length of the `candies` array).

- Finding the maximum number of candies takes **O(n)** time.
- The iteration through the `candies` array also takes **O(n)** time.
- Thus, the overall time complexity is **O(n)**.

### Space Complexity

The space complexity is **O(n)** due to the space used to store the `result` list, where `n` is the number of kids.

- The `result` list contains `n` boolean values, hence using **O(n)** space.
- Other auxiliary space usage, such as the `max_candies` variable, is constant and does not affect the overall space complexity.

Thus, the space complexity is **O(n)**.
---
