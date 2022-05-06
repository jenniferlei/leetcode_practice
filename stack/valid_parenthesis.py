# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

class Solution:
    def valid_parenthesis(self, s) -> bool:
        """
        Checks if string is valid: open brackets are closed and in correct order
        parameter: string (s)
        return: boolean
        """
        # create dictionary to match closing brackets to it's open bracket
        brackets = {")": "(", "}": "{", "]": "["}

        # create empty stack
        open_brackets = []
        # for each char in str, if char is ({[ then add to stack
        for char in s:
            # if char is )}], check if last item in stack is brackets[char]
            if char in brackets:
                if open_brackets and open_brackets[-1] == brackets[char]:
                    open_brackets.pop()
                else:
                    return False
            elif char in brackets.values():
                open_brackets.append(char)
        # if not, return false
        # after loop, if no more open brackets, return true. else return false
        if open_brackets:
            return False
        
        return True


solution = Solution()
print(solution.valid_parenthesis("")) # True
print(solution.valid_parenthesis(")(")) # False
print(solution.valid_parenthesis("}]")) # False
print(solution.valid_parenthesis("({")) # False
print(solution.valid_parenthesis("{}()[]")) # True
print(solution.valid_parenthesis("{)")) # False
print(solution.valid_parenthesis("{([])}()")) # True
print(solution.valid_parenthesis("{([)}()]")) # False
