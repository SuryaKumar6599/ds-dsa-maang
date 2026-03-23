from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        result = [0] * n
        j = 0
        
        for i in range(n):
            if nums[i] != 0:
                result[j] = nums[i]
                j += 1
                
        for k in range(j,n):
            result[k] = 0
            
        for i in range(n):
            nums[i] = result[i]

if __name__ == "__main__":
    nums = [0,1,0,3,12]
    Solution().moveZeroes(nums)
    print(nums)
    
    
#Run command: python 1.move_zeros.py