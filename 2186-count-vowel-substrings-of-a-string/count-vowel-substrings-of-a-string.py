class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        seen=set('aeiou')
        result = 0 
        for i in range(len(word)):
            if word[i] in seen:
                vowels=set()
                for j in range(i,len(word)):
                    if word[j] in seen:
                        vowels.add(word[j])
                        if len(vowels)==5:
                            result+=1
                    else:
                        break 
        return result 
