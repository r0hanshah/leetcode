def containsDuplicate(nums) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
            # nums.remove(num)
            # if num in nums:
            #     return True

        else:
            return False



# Path: leetcode/dup.py
nums = [274,-735,-911,80,454,-511,922,-775,985,-669,-463,-896,-629,-586,910,-361,288,-375,88,556,-578,-406,-87,25,377,-635,-445,-289,646,-962,-487,-924,-968,-962,502,36,129,-611,54,-27,-496,915,-84,-782,349,678,332,-114,345,14,119,710,821,-194,988,38,-369,409,-559,-529,-298,-593,705]

print(containsDuplicate(nums))
