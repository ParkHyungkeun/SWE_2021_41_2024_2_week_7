from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                return[i, j]
nums=[2,7,11,156,8,95,4]
target=164
print(twoSum(nums,target))

            