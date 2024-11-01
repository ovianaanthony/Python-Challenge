class Solution():
    def myAtoi(s):
        a = ''
        i = 0
        j = 0

        while i < len(s):
            if(s[i]=='1' or s[i]=='2' or s[i]=='3' or s[i]=='4' or s[i]=='5' or s[i]=='6' or s[i]=='7' or s[i]=='8' or s[i]=='9' or s[i]=='0'):
                a = a + s[i]
                i+=1
                j+=1
            elif(s[i]==' '):
                i+=1
            elif(s[i]=='-' and j==0):
                j+=1
                a = a + s[i]
                i+=1
            else:
                break
        if(len(a)>0):
            return a
        else:
            return 0

caracter = input('Digite aqui a sequência: ')
print(Solution.myAtoi(caracter))