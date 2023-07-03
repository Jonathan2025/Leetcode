class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # create a an empty results and SORT the numbers since it will be easier to see where we are and which numbers are relatively higher or lower 

        result = []
        nums.sort()

        for i, a in enumerate(nums):
            L = i + 1 # we want the left pointer to be one ahead 
            R = len(nums) - 1

            if i > 0 and a == nums[i-1]: # nums[i] is pretty much the same as "a"
                continue # we want to continue as we dont WANT any duplicates 

            while L < R: 
                sum = a + nums[L] + nums[R]
                if sum > 0:
                    R -= 1
                elif sum < 0:
                    L += 1
                else: 
                    result.append([a, nums[L], nums[R]])
                    L += 1 # we need to move the left pointer to check the possibility that we might have more combinations
                    
                    while nums[L] == nums[L-1] and L < R: # we dont want to ever cross over the R pointer otherwise we will be out of bounds
                        L += 1

        return result 