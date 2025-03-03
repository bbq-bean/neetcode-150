class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # corner cases:
        if s == "" or t == "":
            return False
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        for letter in s:
            if letter not in s_dict:
                s_dict[letter] = 1
            
            else:
                s_dict[letter] += 1
        
        for letter in t:
            if letter not in t_dict:
                t_dict[letter] = 1
            
            else:
                t_dict[letter] += 1
        

        if s_dict == t_dict:
            return True
        
        return False
    
    # O(n) time
    # O(n) space
    