class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if numRows==1:
            return s
        matrix=['']*numRows
        i=0
        gap=numRows-2
        while i<len(s):
            for j in range(numRows):
                if i<len(s):
                    matrix[j]+=s[i]
                    i+=1
            for j in range(gap)[::-1]:
                if j+1>0:
                    if i<len(s):

                        matrix[j+1]+=s[i]
                        i+=1
        ans=''
        for item in range(numRows):
            ans+=matrix[item]
        return ans