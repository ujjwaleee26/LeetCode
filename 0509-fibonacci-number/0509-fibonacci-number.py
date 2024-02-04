class Solution:
    def fib(self, n: int,dp={}) -> int:
        if n in dp:
            return dp[n]
        if n==0:
            return 0
        if n==1:
            return 1
        dp[n]=self.fib(n-1)+self.fib(n-2)  
        return dp[n]  

        