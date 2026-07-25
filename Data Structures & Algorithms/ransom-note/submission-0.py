class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
       countRan = Counter(ransomNote)
       countMag = Counter(magazine)

       for c in countRan:
        if countMag[c] < countRan[c]:
            return False
       return True
    