class Solution():
    
         
    
    def divide(dividend, divisor):            
        a = 0
        if(dividend==divisor):
            return 1
        if((divisor<0 and dividend>0) or (divisor>0 and dividend<0)):
            divisor = -divisor
            a+=1
        if(dividend<0 and divisor<0):
            dividend = -dividend
            divisor = -divisor
        if(dividend>0 and divisor>0):    
            x = 1
            y = divisor
            while divisor <= dividend:
                divisor+=y
                x+=1
            if((divisor>dividend) and a==0):
                divisor-=y
                x-=1
                return x
            elif((divisor>dividend) and a!=0):
                x-=1
                return -x
            elif(a==0):
                return x
            else:
                return -x

dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))
print(Solution.divide(dividendo,divisor))