lar = float(input('Largura da parede '))
alt = float(input(('Altura da parede')))
area = lar*alt
print('Sua parede tem a dimensão de {}x{} e a sua área é de {:.3f}m²'.format(lar,alt,area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {:.3f} de tinta'.format(tinta))

