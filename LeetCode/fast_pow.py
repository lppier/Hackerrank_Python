class Solution:

    def fastPow(self, x, n):
        if n == 0:
            return 1
        print(n)
        half = self.fastPow(x, n//2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x  # since if there is odd x, there is a extra x not multiplied

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        return self.fastPow(x, n)
