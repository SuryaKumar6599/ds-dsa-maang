class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        writePos = 0
        
        for readPos in range(1, len(nums)):
            if nums[readPos] != nums[writePos]:
                writePos += 1
                nums[writePos] = nums[readPos]
        
        return writePos + 1