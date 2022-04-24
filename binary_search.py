# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

def binary_search(nums, target):
    """find target in sorted nums array and return index, otherwise return -1"""

    # [0,2,3,5,7,9], 2 -> 1
    # [0,2,3,5,7,9], 7 -> 4
    # [0,2,3,4,5,7,9], 4 -> 3
    # [], 1 -> -1
    # [1], 1 -> 0
    # [1, 5, 7, 9], 3 -> -1

    left = 0
    right = len(nums) - 1

    # while list:
    while left <= right:
        # // length of list in half
        mid_index = (left + right) // 2

        # if list at index > target, search beginning half of list
        if nums[mid_index] > target:
            right = mid_index - 1
        # otherwise search end of list
        elif nums[mid_index] < target:
            left = mid_index + 1
        # if list at index == target, return index
        else:
            return mid_index
        
        # repeat

    return -1

# [0,2,3,5,7,9], 2 -> 1
print(binary_search([0,2,3,5,7,9], 2))
# [0,2,3,5,7,9], 7 -> 4
print(binary_search([0,2,3,5,7,9], 7))
# [0,2,3,4,5,7,9], 4 -> 3
print(binary_search([0,2,3,4,5,7,9], 4))
# [], 1 -> -1
print(binary_search([], 1))
# [1], 1 -> 0
print(binary_search([1], 1))
# [1, 5, 7, 9], 3 -> -1
print(binary_search([1, 5, 7, 9], 3))