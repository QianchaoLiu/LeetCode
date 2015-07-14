class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        #每n个放到一个深度为n的盒子里，中间即一个深度为1的盒子；
        #读取的时候，从m个盒子里，取第一个，从深度为1的盒子里一个；取3/2=1 5/2=2
        #14/4=3
        if len(s)%numRows==0
            times=len(s)/(numRows+1)
        else:
            times=len(s)/(numRows+1)+1
        matrix=[]
        singlelist=[]
        for i in range(len(times)):
            #i=0,1,2,3
            nlist=[]
            for j in range(len(numRows)):
                #j=0,1,2
                nlist.append(s[i*numRows+j])
                if j==numRows-1:
                    singlelist.append(i*numRows+j+1)
            matrix.append(nlist)
        ans=''
        i=0
        for item in range(len(numRows)):
            if item==numRows/2:
                for line in matrix:
                    s+=line[item]
                    s+=singelist[i]
                    i+=1
            else:
                for line in matrix:
                    s+=line[item]
        return s