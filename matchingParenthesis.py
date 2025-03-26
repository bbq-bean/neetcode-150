class solution:
    def isValid(self, s):
        # check for easy corner cases
        if len(s) % 2 != 0: return False

        # used to determine if a char is a closing parenthesis,
        # and also to check for matches
        paren_dict = {
            ']':'[',
            '}':'{',
            ')':'('
        }

        # they key to this problem
        stack = []

        for char in s:
            if char in paren_dict:
                # this means we found a match, so pop it
                if stack and stack[-1] == paren_dict[char]:
                    stack.pop()
                # otherwise, parenthese cant be valid
                else:
                    return False
            # else keep dumping opening parenthese for checking later
            else:
                stack.append(char)
        
        # if anything is left its not valid
        if stack:
            return False
        
        return True
    
    # O(n) time
    # O(n) space
    