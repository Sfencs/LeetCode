class Solution:
    # 我的low解，提交运行超时。。。。
    def consecutiveNumbersSum(self, N: int) -> int:
        count = 1
        if N == 1:
            return 1
        if N == 2:
            return 1

        temp1 = int(N/2)
        while leijia(temp1) >= N:
            temp2=0
            while leijia(temp1)-leijia(temp2)>=N:
                if leijia(temp1)-leijia(temp2)==N:
                    count += 1
                    break
                else:
                    temp2 += 1
            temp1 -= 1
        if N % 2 == 1:
            count += 1
        return count

    # 别人的，和评论区的思路一样
    def other(self,N):
        result = 0
        k = 1
        while k * (k + 1) <= 2 * N:
            if ((N - k * (k + 1) / 2) % k == 0):
                result += 1
            k += 1
        return result

def leijia(a):
    """累加"""
    if a%2 == 1:
        return int((1+a)*int((a/2))+(1+a)/2)
    else:
        return int((1+a)*(a/2))


