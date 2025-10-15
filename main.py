from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    num_li = {}

    for i, num in enumerate(nums):
        check = target - num
        if check in num_li:
            return [num_li[check], i]
        num_li[num] = i
    
    return []

