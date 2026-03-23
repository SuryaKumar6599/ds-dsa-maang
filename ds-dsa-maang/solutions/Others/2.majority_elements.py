class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Method 1: Sorting
        #Time Complexity: O(nlogn)
        #Space Complexity: O(1)
        nums.sort()
        return nums[len(nums) // 2]
    
        #Method 2: Hash Map
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        #count = {}
        #for num in nums:
            #count[num] = count.get(num, 0) + 1
            #if count[num] > len(nums) // 2:
                #return num
        #return -1  
        #Method 3: Boyer-Moore Voting Algorithm
        #Time Complexity: O(n)
        #Space Complexity: O(1)
        #count = 0
        #candidate = None
        #for num in nums:
            #if count == 0:
                #candidate = num
            #count += (1 if num == candidate else -1)
        #return candidate