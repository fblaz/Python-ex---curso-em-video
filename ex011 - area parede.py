larg = float(input('largura da parede em metros: '))
alt = float(input('altura da parde em metros '))
rend = 2   # rendimento de 2m2 por litro de tinta
area = larg*alt
tinta = area/rend
print(f'a area é de {area} m2 \n'
      f'será necessário comprar {tinta:.2f} litros de tinta')