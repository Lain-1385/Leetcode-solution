class Solution:
    def myPow(self, x: float, n: int) -> float:
        temp = 0
        if n == 0:
            return 1
        # if n == -1 not set, when n < 0 e.g. -4, resursion won't end
        if n == -1:
            return 1/x
        elif n % 2 == 0:
            temp = self.myPow(x, n / 2)
            return temp * temp
        else:
            temp = self.myPow(x, n // 2)
            return temp * temp * x