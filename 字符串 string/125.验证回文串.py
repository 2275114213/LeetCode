"""
https://leetcode-cn.com/problems/valid-palindrome/
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        a = 0
        b = 0
        while i <= j:
            if s[i].isalnum() or s[i].isalpha():
                a = s[i]
                i += 1
            else:
                i += 1
            if s[j].isalpha() or s[j].isalnum():
                b = s[j]
                j -= 1
            else:
                j -= 1

            if a != b:
                return False
        return True


res = Solution().isPalindrome("ab;a")
print(res)
