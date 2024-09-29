class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        temp = str(x)

        return int(temp[::-1]) == x