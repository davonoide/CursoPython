class Ship:
    def __init__(self):
        self.position = 0

    @staticmethod
    def dibujar_inicio_pista():
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|Meta")

    def dibujar_ship(self, desfase, nombre):
        self.position += desfase
        print("                                                                                                                         ")
        print(" " * self.position + nombre)
        print(" " * self.position + "    |    |    |    |")
        print(" " * self.position + "   )_)  )_)  )_)  )_)")
        print(" " * self.position + "  )___))___))___))___)")
        print(" " * self.position + " )____)____)____)_____)")
        print(" " * self.position + "____|____|____|____|____|_")
        print(" " * self.position + "\                   /")
        print(" " * self.position + " \_________________/")
