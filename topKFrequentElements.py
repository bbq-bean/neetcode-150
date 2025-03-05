class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_k = []
        k_dict = {}

        # Create frequency dictionary
        for num in nums:
            k_dict[num] = k_dict.get(num, 0) + 1

        # Find top K frequent elements
        for _ in range(k):
            highest = max(k_dict, key=k_dict.get)  # Get key with highest frequency
            top_k.append(highest)
            del k_dict[highest]  # Remove after adding

        return top_k
       