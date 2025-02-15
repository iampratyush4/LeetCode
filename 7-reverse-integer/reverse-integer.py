class Solution:
    def reverse(self, x: int) -> int:
        if (x >= -(2**31)) and x <= ((2**31) - 1):
            n=abs(x)
            k=0
            while n>0:
                v=n%10
                k=10*k+v
                n=n//10

            if(k <= -(2**31)) or k >= ((2**31) - 1):
                return 0
            
            elif x<0:
                return -k
            else:
                return k
        
        else:
            return 0
        


        