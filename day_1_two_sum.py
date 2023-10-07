"""
Question

Two Sum

Given an array of integers nums and an integer target , return indices
of the two numbers such that they add up to target
You may assume that each input would have exactly one solution, and
you may not use the same element twice.
You can return the answer in any order.
"""


def two_sum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_dict:
            return [num_dict[complement], i]

        num_dict[num] = i

    return []


nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)
