def getCommonPrefix(a,b):
    ret = ''
    for i in range(min(len(a),len(b))):
        if a[i] == b[i]:
            ret += a[i]
        else:
            return ret
    return ret



class Solution:
    # 我的
    def longestCommonPrefix(self, strs) -> str:

        length = len(strs)
        if length == 0:
            return ''
        if length == 1:
            return strs[0]
        result_str = strs[0]
        length = len(strs)
        for n,i in enumerate(strs):

            if n > length-2:
                return result_str
            if strs[n+1] == '' or i == '':
                return ''
            else:
                result_str = getCommonPrefix(result_str,strs[n+1])

    # 这个有点厉害，按字符串排序比最大最小
    def other(self, strs):
        if not strs: return ""
        s1 = min(strs)
        s2 = max(strs)
        for i, x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        return s1



