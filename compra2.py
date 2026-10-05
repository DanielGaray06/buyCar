from os import system
system("cls")

def color(picture):
    if picture == "red":
        exist="3 month"
    elif picture == "white":
        exist= "2 month"
    elif picture == "gray":
            exist= "1 month"
    else:
        exist = "Color not found"
    return exist

def marca(mark):
    if mark == "mazda":
          type = "Mecanical"
    elif mark == "renault":
          type = "Electronic"
    elif mark == "toyota":
          type = "Hybrid"
    else:
         type = "Vehicle type does not exist"
    return type

def plazo (worth, tax):
    worthTotalIva= worth + (worth * tax)
    months = worthTotalIva / 60
    return worthTotalIva

def main():
    c = "s"
    while c == "s" or c == "S":
        system("cls")
        col = input("Ingrese el color del vehiculo: ")
        mar = input("Ingrese la marca del vehiculo: ")
        val = input("Ingrese el valor del vehiculo: ")
        c = color (col)
        m = marca(m)
        p = plazo(val, 0.19)

        if col == "red" or col == "white" or col == "gray":
             if mar == "mazda" or mar == "renault" or mar == "toyota":
                  print ("El color del vehiculo solicitado es: ",c)
                  print ("El tipo del vehiculo solicitado es: ",m)
                  print ("Y el precio del vehiculo solicitado es: ",p)
        else:
            print("*******************************")
            print("PRODUCT DOES NOT EXIST")
            print("")

            c = input ("Si desea continuar presione S: ")
            main ()

