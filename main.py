from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    num_li = {}

    for i, num in enumerate(nums):
        check = target - num
        if check in num_li:
            return [num_li[check], i]
        num_li[num] = i
    
    return []

print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))
