def isPalindrome(self, s: str) -> bool:
    # first clean the string
    s_list = [item.lower() for item in s if item.isalnum()]
    
    # reverse it in a non-builtin way
    s_reverse_list = []
    for i in range(len(s_list) - 1, -1, -1):
        s_reverse_list.append(s_list[i])
    
    # compare the joined strings
    if ''.join(s_list) == ''.join(s_reverse_list):
        return True

    return False

