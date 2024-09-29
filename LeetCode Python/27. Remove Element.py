class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x = nums.copy()
        for num in x:
            if(val in nums):
                nums.remove(val)
        return len(nums)