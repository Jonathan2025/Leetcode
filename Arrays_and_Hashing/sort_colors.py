class Solution:
    def sortColors(self, nums: List[int]) -> None:


        # first initialize the pointers 
        L = 0 
        R = len(nums) - 1
        i = 0 


        while i <= R: # while i has not overlapped with R
            # we have two cases 1) move the left pointer or 2) move the right pointer
            if nums[i] == 0: # if we hit a zero that means we should perform a swap so that it goes on the left side 
                nums[L], nums[i] = nums[i], nums[L]
                L += 1 # move up the left pointer

            elif nums[i] == 2: # if we hit a 2 that means we should perform a swap with the RIGHT pointer. since we want 
                # the 2 to the right 
                nums[R], nums[i] = nums[i], nums[R]
                R -= 1 # we want to move the right pointer 
                i -= 1 # we also want to offset the i pointer because if we move it, then its possible that we move a zero up to the middle which is not what we want 

            i += 1


