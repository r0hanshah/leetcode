class Solution:
    def twoSum(nums, target: int):
        for index,elm in enumerate(nums):
            maxindex = len(nums)-1
            
            if index+1 == len(nums):
                break
            if nums[index] + nums[index+1] == target:
                return [index, index+1]
            if nums[maxindex] + nums[index] != target:
                maxindex -= 1

            if nums[maxindex] + nums[index] == target:
                return [index, maxindex]
        for index,elm in enumerate(nums):
            maxindex = len(nums)-1
            while maxindex > 0:
                if nums[maxindex] + nums[index] == target:
                    return [index, maxindex]
                maxindex -= 1

        
            
nums = [150,24,79,50,88,345,3]
target = 200
print(Solution.twoSum(nums, target))