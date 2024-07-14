class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        nums_x = nums.copy()

        for i in range(1, len(nums_x)):
            if nums_x[i] == nums_x[i - 1]:
                nums.remove(nums_x[i])
        return len(nums)

# Solución creando 2 listas

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        nums = [1,1,2]
        x = nums.copy()
        new=[]

        for i,num in enumerate(nums):
            x.remove(num)
            if(num not in x):
                new.append(num)       
        return len(new)
