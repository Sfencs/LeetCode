class Solution:


    # 我的low解
    def reverse(self, x: int) -> int:
        if x == 0:
            return x

        result_list = []
        a = x
        to_str = None
        if x < 0:
            x = x * (-1)

        while x != 0:
            shang = x // 10
            yushu = x % 10
            result_list.append(yushu)
            x = shang
        if a < 0:

            print(result_list)
            to_str = ''.join([str(i) for i in result_list])
            print(to_str)
            if 2 ** 31 - 1 < int(to_str) * -1 or int(to_str) * -1 < 2 ** 31 * -1:
                return 0
            return int(to_str) * -1
        else:
            print(result_list)
            to_str = ''.join([str(i) for i in result_list])
            print(to_str)
            if 2 ** 31 - 1 < int(to_str) or int(to_str) < 2 ** 31 * -1:
                return 0
            return int(to_str)


    # 别人的
    def other1(self,x):
        if x==0:
            return 0
        str_x = str(x)
        x = ''
        if str_x[0] == '-':
            x += '-'
        x += str_x[len(str_x)-1::-1].lstrip("0").rstrip("-")
        x = int(x)
        if -2**31<x<2**31-1:
            return x
        return 0
