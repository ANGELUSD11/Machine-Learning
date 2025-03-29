class juegoComparativa():
    def __init__(self):
        pass
    def comparativa1(self):
        print("==================================================================")
        print("======================Comparativa frutas==========================")
        print("===============Responda las siguientes preguntas==================")
        print("==================================================================")

        #Preguntas: Dónde nace?, qué vitaminas posee? cómo es su textura?
        frutas = ["Aguacate🥑", "Piña🍍"]
        for fruta in frutas:
            print(f"Fruta: {fruta}")

        print()

        print("Empecemos con las preguntas😃")
        print()
        print("Pregunta 1: ¿Dónde nace la fruta?")
        print("Respuestas:\n1. En clima cálido🌴")
        print("\n2. En clima frío☃️")
        print("\n2. En clima templado🌄")
        print()

        while True:
            try:
                respuesta = int(input("Escoga su respuesta con el número correspondiente: "))
                if respuesta == 1:
                    print("Tu fruta puede ser el aguacate o la piña🥑/🍍?.")
                    print("\nHagamos más preguntas😀")
                elif respuesta == 2:
                    print("Ni el aguacate ni la piña crecen en clima frío🫤")
                else:
                    print("Ni el aguacate ni la piña crecen en clima templado🫤")
                break
            except ValueError:
                print("Por favor ingrese un número entero.")

        print("Pregunta 2: ¿Qué vitaminas posee")
        print("Respuestas:\n1. Vitamina C")
        print("\n2. Vitamina B6")
        print("\n2. Vitamina K")
        print()

        while True:
            try:
                respuesta = int(input("Escoga su respuesta con el número correspondiente: "))
                if respuesta == 1:
                    print("Tu fruta puede ser el aguacate o la piña🥑/🍍?.")
                    print("\nHagamos más preguntas😀.")
                elif respuesta == 3:
                    print("Tu fruta puede ser el aguacate o la piña🥑/🍍?.")
                    print("\nHagamos más preguntas😀.")
                else:
                    print("Tu fruta debe ser la piña🍍😀.")
                    print("Felicidades, haz acertado una fruta😃.")
                    exit()
                break
            except ValueError:
                print("Por favor ingrese un número entero.")

        print("Pregunta 3: ¿Cómo es su textura?")
        print("Respuestas:\n1. Lisa")
        print("\n2. Rugosa")
        print()

        while True:
            try:
                respuesta = int(input("Escoga su respuesta con el número correspondiente: "))
                if respuesta == 1:
                    print("Tu fruta debe ser el aguacate🥑😀.")
                    print("Felicidades, haz acertado una fruta😃.")
                    exit()
                else:
                    print("Tu fruta debe ser la piña🍍😀.")
                    print("Felicidades, haz acertado una fruta😃.")
                    exit()
                break
            except ValueError:
                print("Por favor ingrese un número entero.")

    def comparativa2(self):
        print("======================Comparativa frutas2==========================")
        print("===============Responda las siguientes preguntas==================")

        #Preguntas: Dónde nace?, qué vitaminas posee? cómo es su textura?
        frutas = ["Manzana🍎", "Banano🍌"]
        for fruta in frutas:
            print(f"Fruta: {fruta}")

        print()

        print("Empecemos con las preguntas😃")
        print()
        print("Pregunta 1: ¿Cómo es su sabor?")
        print("Respuestas:\n1. Dulce")
        print("\n2. Ácida")
        print()

        while True:
            try:
                respuesta = int(input("Escoga su respuesta con el número correspondiente: "))
                if respuesta == 1:
                    print("Tu fruta puede ser el la manzana o el banano.")
                    print("\nHagamos más preguntas😀")
                else:
                    print("Tu fruta debe ser la manzana😀")
                    exit()
                break
            except ValueError:
                print("Por favor ingrese un número entero.")

        print("Pregunta 2: ¿Qué tipo de cáscara tiene")
        print("Respuestas:\n1. Firme y delgada")
        print("\n2. Flexible y fácil de pelar")
        print("\n2. Rígida y dura")
        print()

        while True:
            try:
                respuesta = int(input("Escoga su respuesta con el número correspondiente: "))
                if respuesta == 1:
                    print("Tu fruta debe ser la manzana😀.")
                    print("Felicidades, haz acertado una fruta😃.")
                    exit()
                elif respuesta == 2:
                    print("Tu fruta debe ser el banano😀.")
                    print("Felicidades, haz acertado una fruta😃.")
                    exit()
                else:
                    print("Ninguna de las dos cumple con esta característica🫤.")
                    print("\nHagamos más preguntas😀.")
                break
            except ValueError:
                print("Por favor ingrese un número entero.")

        print("Pregunta 3: ¿Cómo se descompone?")
        print("Respuestas:\n1. Se oxida rápidamente y se pone marrón")
        print("\n2. Se vuelve negra y blanda con el tiempo")
        print()

        while True:
            try:
                respuesta = int(input("Escoga su respuesta con el número correspondiente: "))
                if respuesta == 1:
                    print("Tu fruta debe ser la manzana😀.")
                    print("Felicidades, haz acertado una fruta😃.")
                    exit()
                else:
                    print("Tu fruta debe ser el banano😀.")
                    print("Felicidades, haz acertado una fruta😃.")
                    exit()
                break
            except ValueError:
                print("Por favor ingrese un número entero.")

if __name__ == "__main__":
    inicio = input("Desea comparar frutas? (si/no): ").strip().lower()
    if inicio in ["sí", "si", "s"]:
        print("1. Aguacate y piña")
        print("2. Manzana y banano")
        while True:
            try:
                comparar = int(input("Elige qué comparación quieres jugar🤔: "))
                if comparar == 1:
                    juego = juegoComparativa()
                    juego.comparativa1()
                else:
                    juego = juegoComparativa()
                    juego.comparativa2()
            except ValueError:
                print("Por favor ingrese un número entero.")
    else:
        print("Hasta luego!")
        exit()