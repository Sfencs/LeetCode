class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        if len(s) == 1:
            return 1
        length1 = 0
        length = 0
        dict2 = {}
        for n,i in enumerate(s):
           if dict2.get(i) == None:
               dict2[i] = n
               length += 1
               if length>length1:
                   length1 = length
           else:
               if length > length1:
                   length1 = length
               index = dict2[i]
               list = []
               for x in dict2:
                   if dict2[x] < index:
                       list.append(x)
               for y in list:
                   del dict2[y]
               dict2[i] = n
               length = dict2.__len__()
        return length1




    # 别人的神仙算法，，没看懂
    def other(self,s):
        st = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
        return ans





