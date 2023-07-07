'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


'''




class Solution:
    def isAnagram(self, s: str, t: str) -> bool:



        # Here are my approaches
        # 1) We could just sort both of the strings and if they equal, then that means they have to be anagrams of each other
        # return s.sort() == t.sort()

        # return ''.join(sorted(s)) == ''.join(sorted(t))


        # we can also use a way we didnt think of which is using hashmaps for map the frequency 

        hashmap_t = {}
        hashmap_s = {}

        # our base case is if the lengths arent even equal at all 
        if len(s) != len(t):
            return False


        # Now if we pass that we need to see if the hashmap of the frequencies equal to each other
        for character in s: 
            hashmap_s[character] = hashmap_s.get(character, 0) + 1 # so if the character doesnt exist then the frequency will be 0 otherwise get its frequency and then add 1 
        
        for character in t: 
            hashmap_t[character] = hashmap_t.get(character, 0) + 1


        return hashmap_s == hashmap_t
