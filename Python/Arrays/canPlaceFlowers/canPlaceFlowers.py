class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                # Check if the current plot can have a flower:
                # - Either it's the first plot or the previous plot is empty
                # - Either it's the last plot or the next plot is empty
                if (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                    flowerbed[i] = 1
                    # Decrease the number of flowers we still need to plant
                    n -= 1
                    if n == 0:
                        return True
                    # Skip the next plot to respect the no-adjacent-flowers rule
                    i += 1
            i += 1
          
        return n <= 0
