class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

       # Best way is using a Hashmap, this will be the result that is returned --> meaning by default a list value will be returned
        result = defaultdict(list)

       # now we need to loop through each string 
        for s in strs: 

           # Now we want to initiate a count variable. So pretty much for each string we want to have a count of the character frequency 
            count = [0] * 26 # each index will represent a specific letter in the alphabet

           # now loop through each character in that string 
            for c in s: 

               #count[index] += 1 # so now for each character we want to increment the specific index in "count" by 1 
               # in order to do this we will need to use the ord method - which returns an integer representing a UNICODE character
               # Below lets say c is the letter "t". Now if we did ord"t" - "a" we get 122 - 97 which gives us 19 which will be the index 
                count[ord(c) - ord("a")] += 1

            # Now once we go through a string what might we get ?
            #count = [0, 0, 3, 1, 0 ...] we get the relative indexes representing the frequencies of characters
            # in the result dictionary, we first access the specific keys --> represented by frequencies of characters. Then we APPEND the string to that frequency IF the it matches the frequency

            result[tuple(count)].append(s)


        return result