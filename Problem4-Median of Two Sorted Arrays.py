class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        numlist=nums1+nums2
        numlist.sort()
        if len(numlist)%2==0:
            return (float(numlist[len(numlist)/2-1]+numlist[len(numlist)/2]))/2
        else:
            return float(numlist[len(numlist)/2])