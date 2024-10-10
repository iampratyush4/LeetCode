class Solution:
    def isPalindrome(self, x: int) -> bool:

        print(str(x)[::-1])
        if(str(x) == str(x)[::-1]):
            return True
        else:
            return False
        