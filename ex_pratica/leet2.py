class Solution():
    def lengthOfLongestSubstring(s):
        if (len(s)<0 and len(s)>50000):
            return 'limit [0, 50000]'
        else:
            b = ''
            lt = ''
            letra = 0
            while letra < len(s)-1:
                if s[letra] != s[letra+1]:
                    b = b + s[letra]
                    letra+=1
                elif s[letra] == s[letra+1] and letra == 0:
                    letra+=1
                else:
                    b = b + s[letra]
                    if len(lt)<len(b):
                        lt = b
                    b = ''
                    letra+=1
            b = b + s[len(s)-1]
            if(len(lt)>len(b)):
                return lt
            elif(len(lt)==len(b)):
                return lt, b
            else:
                return b

entrada = input()
print(Solution.lengthOfLongestSubstring(entrada))