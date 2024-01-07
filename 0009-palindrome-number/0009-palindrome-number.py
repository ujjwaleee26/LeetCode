class Solution(object):
    def isPalindrome(self, x):
        sum=0
        d=x
        if x<0:
            return False
        else:
            while d>0:
                r=d%10
                sum=sum*10+r
                d//=10
# integer division              
            if sum==x:
                return True
            else:
                return False
            