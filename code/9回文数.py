class Solution:
    def isPalindrome(self, x: int) -> bool:
        int_to_str = str(x)
        length = len(int_to_str)
        for i in range(length):
            if int_to_str[i]==int_to_str[length-i-1]:
                pass
            else:
                return False

        return True




if __name__ == '__main__':
    print(Solution().isPalindrome(-12))