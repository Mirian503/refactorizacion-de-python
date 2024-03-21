def introducir_puntuacion():
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5')
        point = input()
        if point.isdecimal():
            point = int(point)
            if point <= 0 or point > 5:
                print('Por favor, introduzca un valor entre 1 y 5')
            else:
                print('Introduzca sus comentarios.')
                comment = input()
                post = f'punto: {point} comentario: {comment}'
                file_pc = open("data.txt", 'a')
                file_pc.write(f'{post}\n')
                file_pc.close()
                break
        else:
            print('Introduzca los puntos de valoración como números')

def comprobar_resultados():
    print('Resultados hasta la fecha.')
    with open("data.txt", "r") as read_file:
        print(read_file.read())

def main():
    while True:
        print('Seleccione el proceso que desea aplicar')
        print('1: Introducir puntos de evaluación y comentarios')
        print('2: Comprobar los resultados hasta ahora.')
        print('3: Terminar.')
        num = input()

        if num.isdecimal():
            num = int(num)
            if num == 1:
                introducir_puntuacion()
            elif num == 2:
                comprobar_resultados()
            elif num == 3:
                print('Terminación.')
                break
            else:
                print('Introduzca del 1 al 3')
        else:
            print('Introduzca del 1 al 3')

if __name__ == "__main__":
    main()
