class Solution:
    # 我的，巨菜解法。。。
    def romanToInt(self, s: str) -> int:
        dict1 = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        dict2 = {'IV':-2,'IX':-2,'XL':-20,'XC':-20,'CD':-200,'CM':-200}
        return s.count('I')+s.count('V')*5+s.count('X')*10+s.count('L')*50+s.count('C')*100+s.count('D')*500+s.count('M')*1000-s.count('IV')*2-s.count('IX')*2-s.count('XL')*20-s.count('XC')*20-s.count('CD')*200-s.count('CM')*200






