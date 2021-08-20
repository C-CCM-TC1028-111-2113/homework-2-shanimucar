def main():
    # Escribe el código adecuado para completar el programa
    x = int(input("Ingresa el primer número: "))
    y = int(input("Ingresa el segundo número: "))
    z = int(input("Ingresa el tercer número: "))


    if x < y and y < z and x < z:
        print(x)
        print(y)
        print(z)
    elif x < y and x < z and z < y:
        print(x) 
        print(z) 
        print(y)
    elif y < z and y < x and x < z:
        print(y) 
        print(x)
        print(z)
    elif y < z and y < x and z < x:
        print(y)
        print(z)
        print(x)
    elif z < y and z < x and y < x:
        print(z)
        print(y)
        print(x)
    elif z < y and z < x and x < y:
        print(z)
        print(x)
        print(y)
    elif x == y and y ==z:
        print(x)
        print(y)
        print(z)

if __name__=='__main__':
    main()
