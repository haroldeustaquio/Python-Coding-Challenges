class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[j]+nums[i]== target):
                    out.extend([i,j])
        return out