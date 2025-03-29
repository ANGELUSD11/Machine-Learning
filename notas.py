from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt 


#las notas son valores, la entrada numérica que el modelo usa para predecir
notes = [[1],
         [2],
         [2.5],
         [3],
         [3.5],
         [4],
         [4.5],
         [5]]
#los resultados son las clases del modelo, es una categoría en la que el modelo está tratando de clasificar los datos
results = [0,
           0,
           0, 
           1, 
           1, 
           1, 
           1, 
           1]

def training_notes(notes, results):
    model = LogisticRegression()
    model.fit(notes, results)
    rango = np.linspace(0.5, 5.5, 100).reshape(-1, 1)
    print("==================DATOS DEL RANGO=====================")
    print(rango)
    test = model.predict_proba(rango)[:, 1]
    print("==================DATOS DEL LA PREDICCIÓN=====================")
    for valor in test:
        print(valor)
    test_sin_validar = model.predict_proba(rango)
    print("==================DATOS DEL LA PREDICCIÓN SIN VALIDAR=====================")
    for valor in test_sin_validar:
        print(valor)
    plt.figure(figsize=(10, 5))
    plt.scatter(notes, results, color="blue", label="Datos conocidos")
    plt.plot(rango, test, color="green", label="Curva aprendida por la IA")
    plt.axhline(0.5, color="red", linestyle="--", label="límite de decisión(0.5)")
    plt.title("Aprueba o reprueba - aprendizaje supervisado")
    plt.xlabel("Notas del estudiante")
    plt.ylabel("Probabilidad de aprobar")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    return model
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

model = training_notes(notes, results)
show_results(notes, results)
print("\nGracias por usar el sistema de predicción de notas")

while True:
    try:
        entrada = float(input("Ingrese la nota del estudiante (0.0 a 5.0): "))
        if entrada == 0:
            break
        if entrada < 0 or entrada > 5:
            print("La nota debe estar entre 0 y 5")
            continue
        predicción = model.predict([[entrada]])[0]
        if predicción == 1:
            estado = "Aprobado"
        else:
            estado = "Reprobado"

        print(f"El estudiante con nota {entrada} ha {estado}")

        notes.append([entrada])
        results.append(predicción)

        model = training_notes(notes, results)
        show_results(notes, results)
        print("\nGracias por usar el sistema de predicción de notas")
        break

    except ValueError:
        print("Por favor, ingrese un número válido")