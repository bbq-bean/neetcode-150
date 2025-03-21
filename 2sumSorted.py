class Solution:
    def twoSum(self, numbers: List[int], target: Int):
# from a list of numbers, return 2
# list is in ascending order
# probably 2 pointers is better

# brute force
# l = 0
#
# while l < len(numbers):
# for r in range(l + 1, len(numb
# if numbers[l] + numbers[r]
# return [l+1, r+1]
#
#
# l += 1
# O(n^2)
# O(1) space

# 2 pointers solution
# logic:
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
