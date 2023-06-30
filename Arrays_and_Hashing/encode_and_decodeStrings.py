'''

Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and is decoded back to the original list of strings.
Please implement encode and decode

'''



class Solution: 

    def encode(self, strs):
        result = []
        for str in strs: 
            result += str(len(str)) + "#" + str # we want to append to the result 3 things 
                                                # 8#Jonathan - so the length, followed by a delimitter and then the actual string 
        return result 
    


    def decode(self, str): # accepts a single string that was encoded and then returns it DECODED into the words originally

        # First lets initialize a pointer and a result that will be the final result that we return
        result = []
        i = 0 

        while i < len(str): # while we go through the string 
            j = i # we want to initalize the second pointer j which will be first the same as i

            while str[j] != "#": # while we havent gotten the # symbol yet that means we are still getting the LENGTH at the beginning of the string 

                j += 1 # we of course want to increment the j pointer 

            length = int(str[i:j]) # Outside the while loop once we HIT the # symbol then we want to get the length 

            # now that we have the length and hit the # symbol then we want to append the string to the result 
            result.append(str[j+1: j + 1 + length])# we do j + 1 because remember outside the while loop we hit the # symbol which is at j. if we want the word itself we need to go one more

            # then we want to UPDATE the i pointer 

            i = j + 1 + length


        return result 