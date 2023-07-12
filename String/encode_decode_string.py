# Reattempt at this problem with greater understanding of 2 pointers


class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        result = ""
        # write your code here
        for string in strs: 
            result += str(len(string)) + "#" + string
        return result
    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here

        result = []
        # the string we will be working with is in the str itself 

        # for this particular problem we need a 2 pointer. 
        i = 0 # start with i 


        while i < len(str):

            # we need another pointer j 
            j = i # j will be equal to i initially

            # MOST important question is thinking about when the 2 pointers need to move. 
            # We want the i pointer to move to the number length of the string 
            # j pointer should go to the "#" symbol

            while str[j] != "#":
                j += 1

            # now lets say j hits the "#" symbol what then? That means from i to j but not including j 
            # we got the length
            length = int(str[i:j])

            # At this point think about what we have so far 
            # the number length at i 
            # the # symbol at j 
            # now to get the actual string, we need to use these indexes together

            stringItself = str[j + 1: j + length + 1]
            # now append that string to result 
            result.append(stringItself)



            # Now how do we MOVE the i pointer 
            i = j + length +1

        return result 