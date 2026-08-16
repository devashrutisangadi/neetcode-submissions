class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        res = nums1 + nums2
        res.sort()

        tLen = len(res)
        if tLen % 2 == 0:
            return (res[tLen // 2 - 1] + res[tLen // 2]) / 2.0
        else:
            return res[tLen // 2]