from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt

#las notas son valores, la entrada numérica que el modelo usa para predecir
notas = [[1],
         [2],
         [2.5],
         [3],
         [3.5],
         [4],
         [4.5],
         [5]]

#los resultados son las clases del modelo, es una categoría en la que el modelo está tratando de clasificar los datos
resultado = [0,
             0,
             0,
             1,
             1,
             1,
             1,
             1] #0 es reprueba y 1 es aprueba

def entrenamiento_notas(notas, resultado):
    modelo = LogisticRegression()
    modelo.fit(notas, resultado)
    rango = np.linspace(0.5, 5,5, 100).reshape(-1, 1)
    print("==================DATOS DEL RANGO=====================")
    print(rango)
    print("==================DATOS DEL LA PREDICCIÓN VALIDADO=====================")
    prueba = modelo.predict_proba(rango)[:, 1]
    for valor in prueba:
        print(valor)
    plt.figure(figsize=(10, 5))
    plt.scatter(notas, resultado, color="blue", label="Datos conocidos")
    plt.plot(rango, prueba, color="green", label="Curva aprendida por la IA")
    plt.axhline(0.5, color="red", linestyle="--", label="límite de decisión(0.5)")
    plt.title("Aprueba o reprueba - aprendizaje supervisado")
    plt.xlabel("Notas del estudiante")
    plt.ylabel("Probabilidad de aprobar")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
    return modelo

def show_results(notes, results):
    print(f"\nLista de notas registradas:")
    print("-" * 35)
    print("N | Nota | Resultado")
    print("-" * 35)

    for i in range(len(notes)):
        if results[i] == 1:
            estado = "Aprueba"
        else:
            estado = "Reprueba"
        print(f"{i+1:>2} | {notes[i][0]:>4.1f} | {estado}")
    print("-" * 35) 

model = entrenamiento_notas(notas, resultado)
show_results(notas, resultado)
print("\nGracias por usar el sistema de predicción de notas")

while True:
    try:
        entrada = float(input("Ingrese la nota del estudiante (0 a 5): "))
        if entrada == 0:
            break
        if entrada < 0 or entrada > 5:
            print("Por favor, escriba un número entre 0 y 5")
            continue
        predicción = model.predict([[entrada]])[0]
        if predicción == 1:
            estado = "Aprueba"
        else:
            estado = "Reprueba"

        print(f"La predicción para la nota {entrada} es {estado}")

        notas.append([entrada])
        resultado.append(predicción)

        model = entrenamiento_notas(notas, resultado)
        show_results(notas, resultado)

        print("Gracias por usar el sistema de predicción de notas")

    except ValueError:
        print("Por favor, escriba un número válido")    