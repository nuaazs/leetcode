# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         # my solution
#         # expand string according to Manacher algorithm
#         # but extend radius step by step
#         ls = len(s)
#         if ls <= 1 or len(set(s)) == 1:
#             return s
#         # create a new list like this: "abc"->"a#b#c"
#         temp_s = '#'.join('{}'.format(s))
#         # print temp_s
#         tls = len(temp_s)
#         seed = range(1, tls - 1)
#         # this table stores the max length palindrome
#         len_table = [0] * tls
#         for step in range(1, tls / 2 + 1):
#             final = []
#             for pos in seed:
#                 if pos - step < 0 or pos + step >= tls:
#                     continue
#                 if temp_s[pos - step] != temp_s[pos + step]:
#                     continue
#                 final.append(pos)
#                 if temp_s[pos - step] == '#':
#                     continue
#                 len_table[pos] = step
#             seed = final
#         max_pos, max_step = 0, 0
#         for i, s in enumerate(len_table):
#             if s >= max_step:
#                 max_step = s
#                 max_pos = i
#         return temp_s[max_pos - max_step:max_pos + max_step + 1].translate(None, '#')

#     # def longestPalindrome(self, s):
#     #     # example in leetcode book
#     #     max_left, max_right = 0, 0
#     #     ls = len(s)
#     #     for i in range(ls):
#     #         len1 = self.expandAroundCenter(s, i, i)
#     #         len2 = self.expandAroundCenter(s, i, i + 1)
#     #         max_len = max(len1, len2)
#     #         if (max_len > max_right - max_left):
#     #             max_left = i - (max_len - 1) / 2
#     #             max_right = i + max_len / 2
#     #     return s[max_left:max_right + 1]
#     #
#     # def expandAroundCenter(self, s, left, right):
#     #     ls = len(s)
#     #     while (left >= 0 and right < ls and s[left] == s[right]):
#     #         left -= 1
#     #         right += 1
#     #     return right - left - 1

#     # def longestPalindrome(self, s):
#     #     #Manacher algorithm
#     #     #http://en.wikipedia.org/wiki/Longest_palindromic_substring
#     #     # Transform S into T.
#     #     # For example, S = "abba", T = "^#a#b#b#a#$".
#     #     # ^ and $ signs are sentinels appended to each end to avoid bounds checking
#     #     T = '#'.join('^{}$'.format(s))
#     #     n = len(T)
#     #     P = [0] * n
#     #     C = R = 0
#     #     for i in range (1, n-1):
#     #         P[i] = (R > i) and min(R - i, P[2*C - i]) # equals to i' = C - (i-C)
#     #         # Attempt to expand palindrome centered at i
#     #         while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
#     #             P[i] += 1
#     #
#     #         # If palindrome centered at i expand past R,
#     #         # adjust center based on expanded palindrome.
#     #         if i + P[i] > R:
#     #             C, R = i, i + P[i]
#     #
#     #     # Find the maximum element in P.
#     #     maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
#     #     return s[(centerIndex - maxLen)//2: (centerIndex + maxLen)//2]

#     # 动态规划 DP 算法：4516 ms	21.7 MB	python3
#     # class Solution:
#     #     def longestPalindrome(self, s: str) -> str:
#     #         dp = [[False]*len(s) for _ in range(len(s))]
#     #         for i in range(len(s)):
#     #             dp[i][i]=True
#     #             logest_palindrom=s[i]
#     #         ans=s[0]
#     #         for j in range(len(s)):
#     #             for i in range(j):
#     #                 if s[i] == s[j] and (dp[i+1][j-1] or j==i+1):
#     #                     dp[i][j] = True
#     #                     if j-i+1>len(ans):
#     #                         ans = s[i:j+1]
#     #         return ans


# 1016 ms	14.4 MB	python3
class Solution:
    def longestPalindrome(self, s: str) -> str:
        p = ''
        for i in range(len(s)):
            p1 = self.get_palindrome(s, i, i+1)
            p2 = self.get_palindrome(s, i, i)
            p = max([p, p1, p2], key=lambda x: len(x))
        return p
    
    def get_palindrome(self, s: str, l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

# 96 ms	14.4 MB
class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if len(s)==0:
        	return 0
        maxLen=1
        start=0
        for i in range(len(s)):
        	if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
        		start=i-maxLen-1
        		maxLen+=2
        		continue

        	if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
        		start=i-maxLen
        		maxLen+=1
        return s[start:start+maxLen]
        
if __name__ == '__main__':
    # begin
    s = Solution()
    print s.longestPalindrome("abcbe")