class Solution:
    # @return an integer

    # def reverse(self, x):
    #     max_int = 2147483647
    #     if x == 0:
    #         return 0
    #     isPos = True
    #     if x < 0:
    #         x *= (-1)
    #         isPos = False
    #     ltemp = []
    #     while x != 0:
    #         temp = x % 10
    #         ltemp.append(temp)
    #         x /= 10
    #     result = 0
    #     # the main solution
    #     for t in ltemp:
    #         result = result * 10 + t
    #     if result > max_int:
    #         result = 0
    #     if isPos:
    #         return result
    #     else:
    #         return -1 * result

    def reverse(self, x):
        # Note that in Python -1 / 10 = -1
        res, isPos = 0, 1
        if x < 0:
            isPos = -1
            x = -1 * x
        while x != 0:
            res = res * 10 + x % 10
            if res > 2147483647:
                return 0
            x /= 10
        return res * isPos

#	32 ms	14.2 MB
class Solution:
    def reverse(self, x: int) -> int:
        rev = int(str(abs(x))[::-1])
        return (-rev if x < 0 else rev) if rev.bit_length() < 32 else 0