
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        L = 0
        result = []
        charMap = {}
        pCharMap = Counter(p)

        for R in range(len(s)):
            # Increment the charMap for each character in the window
            charMap[s[R]] = charMap.get(s[R], 0) + 1

            # Shrink the window until it matches the size of p. The code may seem weird but it makes sense 
            # as we make L bigger ( by shifting the L pointer) we are subtracting byt a bigger L and therefore shrinks the window size
            while R - L + 1 > len(p):
                charMap[s[L]] -= 1
                if charMap[s[L]] == 0:
                    del charMap[s[L]]
                L += 1

            # Check if we have an anagram
            if pCharMap == charMap:
                result.append(L)

        return result