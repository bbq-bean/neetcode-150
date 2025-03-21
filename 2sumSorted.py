class Solution:
    def twoSum(self, numbers: List[int], target: Int):
# numbers are sorted, and we KNOW ther
# so if current sum is less, get a big
# if its more, try a smaller number
        l = 0
        r = len(numbers) - 1
        
        while l < r:
            current_sum = numbers[l] + numbers
            if current_sum < target:
                l += 1
            elif current_sum > target:
                r -= 1
            else:
                return [l+1, r+1]
    # O(n) time
    # O(1) space
