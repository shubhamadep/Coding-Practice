class Solution:
    def threeSum(self, nums):
        n, nums = len(nums), sorted(nums)
        result = []

        for i in range(n-2):
            if i > 0 and nums[i] != nums[i-1] or i == 0:
                j = i+1
                k = n-1
                while j < k:
                    tempsum = nums[j] + nums[k]
                    if  tempsum < -nums[i]: j += 1
                    elif tempsum > -nums[i]: k -= 1
                    else:
                        result.append([nums[i], nums[j], nums[k]])
                        while j < k and nums[j] == nums[j+1]: j += 1
                        while j < k and nums[k] == nums[k-1]: k -= 1
                        j += 1
                        k -= 1
        return result

#TC: O(n**2)
