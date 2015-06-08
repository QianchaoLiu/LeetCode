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
                
#the brief edition
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        scanned = {}
        for j, item in enumerate(nums, 1):
            i = scanned.get(target - item, -1)
            if i > 0:
                return [i, j]
            scanned[item] = j
            
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
                        answers.extend([i+1,flag+1])
                        return answers
                        break
                    
