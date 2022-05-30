# Esta variable representa la hemoglobina
homo = float(input())
#esta es la variable que representa el genero
#1 : masculino 2:femenino
genero = int(input())

if genero == 1 or genero == 2:
    
    if genero == 1:
        if homo  <  13.2:
            print(f'Alerta 1')
        elif homo >= 13.2 and homo <= 16.6:
            print(f'Sin alerta')
        elif homo > 16.6:
            print(f'Alerta 2')
    else:
        if homo < 11.6:
            print(f'Alerta 1')
        elif homo >= 11.6 and homo <= 15.0:
            print(f'Sin alerta')
        elif homo  > 15.0:
            print(f'Alerta 2')
else:
    print(f'No es posible generar la alerta')
