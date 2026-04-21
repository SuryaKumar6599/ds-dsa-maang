"""Given two strings word1 and word2, merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string. """

class Solution:
    def mergeAlternatively(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)
        result = []
        i = j = 0
        
        while i<m or j<n:
            if i<m:
                result += word1[i]
                i+=1
            if j<n:
                result += word2[j]
                j += 1
                
        return "".join(result)