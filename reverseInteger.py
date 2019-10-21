class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        number = int(str(abs(x))[::-1])
        mina = -2**31  
        maxa = 2**31 - 1  
        if number not in range(mina, maxa):  
            return 0  
        return number * sign
