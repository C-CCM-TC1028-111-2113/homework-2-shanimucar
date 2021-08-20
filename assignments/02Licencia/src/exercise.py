
def main():
    #Escribe tu código debajo de esta línea

    edad = int(input("Ingresa tu edad: "))


    if edad >= 18:
        identificación = str(input("¿Tienes identificación oficial? (s/n): "))
        if identificación == ('s'):
            print('Trámite de licencia concedido')
        elif identificación == ('n'):
            print('No cumples requisitos')
        elif identificación != ('s') or ('n'):
            print('Respuesta incorrecta')
    elif edad <18 and edad>0:
        print("No cumples requisitos")
    elif edad <= 0:
        print("Respuesta incorrecta")    





if __name__ == '__main__':
    main()
