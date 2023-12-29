valor = float(input('Digite um valor '))
des = valor*(5/100)
nvpreco = valor-des
print('O valor de {} , resultou em {:.2f} de desconto, o novo preço é {:.2f}'.format(valor,des,nvpreco))
