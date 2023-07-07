# my solutions to the leetcode problem longest common prefix 
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        '''
        FIRST SOLUTION


       # our base case is that if we have no strings at all we can jsut return ""

        if not strs:
            return ""

        # first lets establish some variables

        longest_prefix = ""
        shortest_str = min(strs, key=len) # get the shortest string 
        strs.remove(shortest_str) # we want to remove the shortest str from the strs so we dont need to iterate through it 

        # basically we will iterate through each string at the position of i 
        for i in range(len(shortest_str)):

            for string in strs:

                if string[i] != shortest_str[i]:
                    # if we dont have a match at one of the characters for any of the strings then we just return what we currently have for the prefix and it ends here 
                    return longest_prefix

            # now before we move on the next position, if we made it through the loop so far, we need to add the character to the prefix 
            longest_prefix += shortest_str[i]

        return longest_prefix


        '''


        # second solution 

        # INSTEAD of doing what we did above, what we can do instead is use the first strin/word as the index and if it doesnt match with the other words we can just keep taking off one letter until we find an matching index 

        if not strs:
            return ""

        prefix = strs[0] # we will initalize the prefix as the first string 

        for string in strs[1:]: # for the strings after the first one 

            # while we dont start with the prefix then we take out a letter from the end 
            while not string.startswith(prefix):
                prefix = prefix[:-1]


                # if we eventually come to an empty prefix just return it 
                if not prefix: 
                    return ""

        return prefix