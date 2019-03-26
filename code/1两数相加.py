class Solution:
    # 我的low的办法
    def twoSum(self, nums, target):
        n = len(nums)
        for ind,i in enumerate(sorted(nums)):
            if target-i in nums:
                if target-i == i and ind != n-1:
                    temp = nums[ind+1:-1]
                    for j in temp:
                        if j == i:
                            return [ind, temp.index(target - i)+ind+1]
                else:
                    return [ind, nums.index(target - i)]
    # 别人的1
    def other1(self, nums, target):
        for ind,i in enumerate(nums):
            num = target - i
            try:
                if ind != nums.index(num):
                    return [ind, nums.index(num)]
            except:
                pass

    # 别人的2
    def other2(self, nums, target):
        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None