# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def contains_duplicate(nums):
    """checks if duplicate num in list
    parameter: list of nums
    return: boolean (true if duplicate, false otherwise)"""

    # use empty set
    # loop through nums
        # if num in set, then return true
        # add num to set
    # return false

    seen = set() # time O(1), space O(n)

    for num in nums: # O(n)
        if num in seen: # O(1)
            return True
        seen.add(num) # O(1)

    return False

test_list1 = [] # return False
test_list2 = [1] # return False
test_list3 = [1, 1] # return True
test_list4 = [1, 2, 3, 4] # return False

print(contains_duplicate(test_list1))
print(contains_duplicate(test_list2))
print(contains_duplicate(test_list3))
print(contains_duplicate(test_list4))

# This is O(n) time and O(n) space