print('Proporcione los siguientes datos del libro')
nombreLibro = input('Ingrese el nombre del libro: ')
idLibro = int(input('Proporcione el Id: '))
precio = float(input('Proporcione el valor del libro: '))
envio = input('Desea un envio gratuito? (Indique True/False): ')

print(f'Nombre: {nombreLibro}')
print(f'Id: {idLibro}')
print(f'Precio: $AR{precio}')

if envio == True:

    print('Envio Gratuito? = Aceptado')
else:
    print('Envio Gratuito =: Denegado')
