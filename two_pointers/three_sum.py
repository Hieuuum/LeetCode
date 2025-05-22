#15. 3Sum (Medium)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Used solution
        nums = sorted(nums)
        nums_len = len(nums)
        res = []
        print(nums)
        for i in range(nums_len-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = nums_len - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while nums[j] == nums[j-1] and j < k:
                        j += 1

        return res