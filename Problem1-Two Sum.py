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

#another answer with a lower efficiency
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
            newlist=[]
            answers = []
            for flag, num in enumerate(nums):
                newlist.append(num)
                if newlist.__contains__(target - num):
                    i = newlist.index(target - num)
                    if i<flag:
                        answers.append(i+1)
                        answers.append(flag+1)
                        return answers
                        break
