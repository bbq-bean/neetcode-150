class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # need something that will sort and compare easy
        # how about a dict where the key is the sorted anagram
        # and the entry is a list of anagrams
        ans = []
        an_dict = {}

        # eg
        # {"abc": ["abc", "bac", "cba"]}

        for a in strs:
            sorted_a = ''.join(sorted(a))
            if sorted_a in an_dict:
                # in the test cases, they want duplicates also logged,
                # so no need to check if it already exists in the list
                an_dict[sorted_a].append(a)
            
            else:
                # else make an entry with our sorted key and current anagram
                an_dict[sorted_a] = [a]
        
        for v in an_dict.values():
            ans.append(v)
        
        return ans
