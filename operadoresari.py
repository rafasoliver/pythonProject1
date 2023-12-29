n1 = int(input('Digite o primeiro valor : '))
n2 = int(input('Digite o segundo valor : '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
pt = n1 ** n2
print('a soma {} , o produto {} , divisão {:.2f} '.format(s,m,d))
print('divisão por inteiro {}, e potência {}'.format(di,pt))