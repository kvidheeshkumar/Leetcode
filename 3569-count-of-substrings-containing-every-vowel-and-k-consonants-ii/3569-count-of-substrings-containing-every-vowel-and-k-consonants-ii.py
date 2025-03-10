class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n=len(word)
        vowels=set('aeiou')
        vowelCount=defaultdict(int)
        cons=0
        left=count=substr=0
        def minus(c):
            if c in vowels:
                vowelCount[c]-=1
                if vowelCount[c]==0:
                    del vowelCount[c]
            else:
                nonlocal cons
                cons-=1
        for c in word:
            if c in vowels:
                vowelCount[c]+=1
            else:
                cons+=1
                count=0
            while cons>k:
                minus(word[left])
                left+=1
            while cons==k and len(vowelCount)==5:
                count+=1
                minus(word[left])
                left+=1
            substr+=count
        return substr
        