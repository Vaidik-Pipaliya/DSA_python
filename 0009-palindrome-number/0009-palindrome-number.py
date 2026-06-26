class Solution(object):
    def isPalindrome(self , x):
        num = x
        result = 0
        if num < 0:
            return False
        while num > 0:
            last_digit = num % 10
            result = (result * 10) + last_digit
            num = num // 10
        return result == x



"""class Solution(object):
    def isPalindrome(self, x):
        a = str(x)
        return a == a[::-1]"""
        
