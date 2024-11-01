class Solution:
    def reverse(x):
        if int(x) > 2147483647 or int(x)<-2147483647:
            return '[-2^31, 2^31 - 1] 0'
        if int(x)>=0:   
            i = len(x)-1
            a = []
            b = ''
            c = 0
            while i >= 0:
                a.append(x[i])
                i-=1
                b = b + a[c]
                c+=1
            return int(b)
        else:
            i = len(x)-1
            a = []
            b = '-'
            c = 0
            while i > 0:
                a.append(x[i])
                i-=1
                b = b + a[c]
                c+=1
            return int(b)
        
numero = input('Digite o número desejado: ')
print(Solution.reverse(numero))
