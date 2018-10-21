a = int(input('(a)x:'))
a2 = int(input('(a)x2:'))
b = int(input('(b)x:'))
b2 = int(input('(b)x2:'))
c = int(input('(c)x:'))
c2 = int(input('(c)x2:'))
#算出a,b,c所涵蓋的範圍
result_of_abc = a,a2,b,b2,c,c2
result1 = max(result_of_abc)
result2 = min(result_of_abc)
result = result1-result2
print(abs(result))
