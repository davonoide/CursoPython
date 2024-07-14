import os 
import random
import time
from ship import Ship

def limpiar_consola():

    if os.name =='nt':
        os.system("cls")
    else:
        os.system('clear')

def main():
    bus_1 = Ship()
    bus_2 = Ship()
    print("Batle ship race")


    while True:
        limpiar_consola()
        Ship.dibujar_inicio_pista()
        bus_1.dibujar_ship(random.randint(1,2), "Perla Negra")
        Ship.dibujar_inicio_pista()
        bus_2.dibujar_ship(random.randint(1,2), "Holandez Herrante")
        Ship.dibujar_inicio_pista()

        if bus_1.position >=100 or bus_2.position >=100:
            if bus_1.position == bus_2.position:
                print("############EMPATE############")
                break
            if bus_1.position >= 100:
                print("$$$$$$$$$$$$$$$$Perla Negra ganó!!$$$$$$$$$$$$$$$$")
            else:
                print("$$$$$$$$$$$$$$$$Holandez Herrante ganó!!$$$$$$$$$$$$$$$$")
            break
        time.sleep(.1)

main()