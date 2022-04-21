# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

def two_sum(nums, target):
    """return indices of the two numbers such that they add up to target
    parameters: list of ints, int
    return: list of 2 indexes"""

    # create empty dictionary to keep track of target - num and index
    difference_indexes = {}

    # for each num in nums
    for i, num in enumerate(nums): 
        if num in difference_indexes:
            return [difference_indexes[num], i]
        difference_indexes[(target - num)] = i
    # so for [1, 2, 3, 4] with target 3
    # {2: 0, 1: 1, 0: 3, -1: 4} if loop through all
    # check if num is already in dictionary
    # if true, return [dict[num], index]
    return


nums1 = [1, 2, 3, 4]
target1 = 3
# [0, 1]
print(two_sum(nums1, target1))

nums2 = [3, 3]
target2 = 6
# [0, 1]
print(two_sum(nums2, target2))

nums3 = [1, 5]