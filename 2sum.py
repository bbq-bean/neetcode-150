class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # back to pythonmnnnnnnnnn
        seent = {}

        # for eacho num get the target diff
        for i, num in enumerate(nums):
            diff = target - num

            # if the diff in seent already, we know the answer
            if diff in seent:
                return seent[diff], i

            # else put current num:index in the hashmap 
            seent[num] = i

        # Time Complexity - O(n) the main loops only 1 time
        # Space Complexity - O(n) linear also following worst case size of seent {}
