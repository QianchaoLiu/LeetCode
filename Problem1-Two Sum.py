class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        hashlist = {}
        for index in range(len(nums)):
            if hashlist.get(nums[index]) == None:
                hashlist[nums[index]] = index
            i=hashlist.get(target-nums[index])
            if i!=None and i<index:
                    list=[]
                    list.append(i+1)
                    list.append(index+1)
                    return list
                    break