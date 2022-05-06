# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

def valid_palindrome(s):
    """
    checks if string is same forward and backward
    parameter: string
    returns: boolean
    """
    # edge case: length < 2, return true
    if len(s) < 2:
        return True
    
    # convert to lower
    # remove non-alphanumeric
    str = "".join(char for char in s if char.isalnum()).lower()

    # divide length in half
    # two pointers, i = index 0 and j = index = length of s
    i, j = 0, len(str) - 1
    # while pointers are not the same
    while i != j:
    # if char at first index != char last index, return false
        if str[i] != str[j]:
            return False
    # i + 1, j -1
        i += 1
        j -= 1

    return True

    # example: abc1ded1cba
    # 

s1 = "a"
# true
print(valid_palindrome(s1))

s2 = " "
# true
print(valid_palindrome(s2))

s3 = "Abc1ded1cba!!"
# true
print(valid_palindrome(s3))

s4 = "hello"
# false
print(valid_palindrome(s4))


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """checks if valid palindrome"""
        i, j = 0, len(s) - 1
        
        while i < j:
            while i < j and not self.alphaNum(s[i]):
                i += 1
            while i < j and not self.alphaNum(s[j]):
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1

        return True


    def alphaNum(self, c):
        return (ord("A") <= ord(c) <= ord("Z")
               or ord("a") <= ord(c) <= ord("z")
               or ord("0") <= ord(c) <= ord("9"))

solution = Solution()

print(solution.isPalindrome("a"))
# true

print(solution.isPalindrome(" "))
# true

print(solution.isPalindrome("Abc1ded1cba!!"))
# true

print(solution.isPalindrome("hello"))
# false