class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #2 pointers, add the first and last number and compare with                 target
        l,r = 0, len(numbers)-1
        
        while l <r:
            currSum = numbers[l] + numbers[r]
            if currSum > target:
                r -= 1
            elif currSum < target:
                l += 1
            else: 
                return [l + 1, r + 1]
        return[]