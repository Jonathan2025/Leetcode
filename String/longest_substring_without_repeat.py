class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Pattern - basically we will have a L and R pointer, the R pointer will keep moving BUT L pointer will only move if we have a duplicate. Why use a set? because its generally more efficient

        L = 0 
        charSet = set() # the set will allow us to determine IF we have a duplicate
        longestStringLen = 0 


        for R in range(len(s)):

            # Break things down. 1) we can have a R pointer on a value that is a duplicate OR not a duplicate

            while s[R] in charSet: # why use a while loop, because lets say we need to remove a character duplicate, we need to Keep removing until we hit it 

                charSet.remove(s[L]) # remove the left pointer
                L += 1 # move up the left pointer
            


            #if its not a duplicate then we should ADD it to the set 
            charSet.add(s[R])


            # Now we also need to update the longestSubstring each time 
            longestStringLen = max(longestStringLen, R - L + 1)

        return longestStringLen

            


        





 