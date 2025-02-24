class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seent = []
        for num in nums:
            if num in seent:
                return True
            
            seent.append(num)
        
        return False

        # Time Complexity - O(n) the main loops only 1 time
        # Space Complexity - O(n) linear also following worst case size of seent []