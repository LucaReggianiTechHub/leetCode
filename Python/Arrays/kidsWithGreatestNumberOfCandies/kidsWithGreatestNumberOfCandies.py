class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        
        # Find the maximum number of candies any kid currently has
        max_candies = max(candies)
        
        for candy in candies:
            # Check if the current kid, after receiving the extra candies, 
            # will have at least as many candies as the kid with the most candies
            if candy + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
              
        return result
