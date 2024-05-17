class Solution:
    def isHappy(self, n: int) -> bool:
        k=n
        l=[]
        
        while k > 3:
            if k**2>9:

                h=0
                
                for i in str(k) :
                    h = int(i)**2 + h
            else:
                return False
            k=h
            print(l)
            if k in l:
                return False
            l.append(h)
            
        if k == 1:
            return True
        else:
            return False

            
            
            
            
            
            
                





        