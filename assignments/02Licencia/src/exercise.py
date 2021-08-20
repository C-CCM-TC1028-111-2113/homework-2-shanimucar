
def main():
    #Escribe tu código debajo de esta línea
    edad = int(input("Ingresa tu edad: "))
    identificación = str(input("¿Tienes identificación oficial? (s/n): "))

    if edad >= 18:                  
        if identificación == ('s'):
            print('Trámite de licencia concedido')
        elif identificación == ('n'):
            print('No cumples requisitos')
        else:
            print('Respuesta incorrecta')
    elif edad < 18:
    print("No cumples requisitos")






if __name__ == '__main__':
    main()
