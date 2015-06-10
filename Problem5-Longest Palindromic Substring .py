class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        if len(s)<=1:
            return s
        else:
            def isPalindrome(st):
                if len(st)>=2:
                    if st[0]==st[len(st)-1]:
                        return 1*isPalindrome(st[1:len(st)-1])
                    else:
                        return 0
                else:
                    return 1
            ans=''
            usedlist={}
            for num in range(len(s)):
                if usedlist.get(s[num])!=None:
                    for item in usedlist[s[num]]:
                        if isPalindrome(s[item:num+1]) == 1:
                            ans = s[item:num+1] if num+1-item+1 > len(ans) else ans
                if usedlist.get(s[num])==None:
                    usedlist[s[num]]=[]
                    usedlist[s[num]].append(num)
                else:
                    usedlist[s[num]].append(num)
            return ans
    #above is ELT

    
    def longestPalindrome(self, s):
        new_string = '#'.join('^{}$'.format(s))
        n = len(new_string)
        P = [0] * n
        C = R = 0
        for i in range (1, n-1):
            P[i] = (R > i) and min(R - i, P[2*C - i]) # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while new_string[i + 1 + P[i]] == new_string[i - 1 - P[i]]:
                P[i] += 1

            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]

        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))

        return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]