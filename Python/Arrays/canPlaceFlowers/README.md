# Can Place Flowers - Difficulty Level: Easy

## Problem Statement

You have a long flowerbed in which some of the plots are planted, and some are not. However, **flowers cannot be planted in adjacent plots**.

Given an integer array `flowerbed` containing `0`'s and `1`'s, where `0` means empty and `1` means not empty, and an integer `n`, return `true` if `n` new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and `false` otherwise.

### Examples

#### Example 1:

**Input**:  
`flowerbed = [1,0,0,0,1], n = 1`  
**Output**:  
`true`

**Explanation**:  
We can plant one flower at position `2` without violating the rule.

#### Example 2:

**Input**:  
`flowerbed = [1,0,0,0,1], n = 2`  
**Output**:  
`false`

**Explanation**:  
We can only plant one flower at position `2`, so we cannot plant two flowers.

---

## Intuition

The problem requires determining if it's possible to plant `n` new flowers in a flowerbed without violating the no-adjacent-flowers rule.

### Observations:

1. **Flower Planting Rule**: A flower can be planted in an empty plot (`0`) only if both its adjacent plots are empty or non-existent (for edge plots).

2. **Edge Plots Consideration**: The first and last plots have only one neighbor, so we need to handle these cases carefully.

3. **Optimizing Placement**: To maximize the number of flowers planted, we should plant a flower whenever the rule allows.

---

## Approach

1. **Initialize Index**:

   - Start with an index `i = 0` to iterate through the `flowerbed` array.

2. **Iterate Through the Flowerbed**:

   - **While** `i < len(flowerbed)`:

     a. **Check if Current Plot is Empty**:

        - **If** `flowerbed[i] == 0`:

          i. **Check Adjacent Plots**:

             - **Previous Plot**:
               - **If** `i == 0`, there's no previous plot (consider it as `0`).
               - **Else**, check if `flowerbed[i - 1] == 0`.

             - **Next Plot**:
               - **If** `i == len(flowerbed) - 1`, there's no next plot (consider it as `0`).
               - **Else**, check if `flowerbed[i + 1] == 0`.

          ii. **Determine if Flower Can Be Planted**:

             - **If** both adjacent plots are `0` (empty) or don't exist:
               - Plant a flower at position `i` by setting `flowerbed[i] = 1`.
               - Decrement `n` by `1`.

             - **Early Termination**:
               - **If** `n == 0`, all required flowers have been planted.
                 - **Return** `True`.

             - **Skip Next Plot**:
               - Increment `i` by `1` to skip the next plot, as we can't plant adjacent flowers.

     b. **Move to Next Plot**:

        - Increment `i` by `1` to check the next plot.

3. **Return the Result**:

   - **After** the loop:
     - **If** `n <= 0`, we've planted all required flowers.
       - **Return** `True`.
     - **Else**, we couldn't plant all flowers.
       - **Return** `False`.

---

## Complexity

### Time Complexity

- **O(n)**, where `n` is the length of the flowerbed.
  - We traverse the flowerbed once.
  - In the worst case, we might skip some plots when we plant a flower.

### Space Complexity

- **O(1)**.
  - We modify the input array in place.
  - Only constant extra space is used for variables.
