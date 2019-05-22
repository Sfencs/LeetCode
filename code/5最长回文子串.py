class Solution:


    # 马拉车，参考https://www.cnblogs.com/grandyang/p/4475985.html
    def longestPalindrome(self, s: str) -> str:
        new_s = '$#'
        for i in s:
            new_s = new_s+i+'#'
        mx = 0
        id = 0
        resLen = 0
        resCenter = 0
        p = [0]*len(new_s)
        for i in range(1,len(new_s)):
            p[i] = min(p[2 * id - i], mx - i) if mx > i else 1

            try:
                while new_s[i + p[i]] == new_s[i - p[i]]:
                    p[i] += 1
            except:
                pass
            if mx < i + p[i]:
                mx = i + p[i]
                id = i

            if resLen < p[i]:
                resLen = p[i]
                resCenter = i
        return s[int((resCenter - resLen) / 2): int((resCenter - resLen) / 2)+resLen - 1]


