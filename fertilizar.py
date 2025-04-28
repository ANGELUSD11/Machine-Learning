import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

#variables de entrada
humedad = np.arange(0, 101, 1)
nutrientes = np.arange(0, 101, 1)
fertilizacion = np.arange(0, 101, 1)

#funciones de pertenencia para la humedad
humedad_baja = fuzz.trimf(humedad, [0, 15, 30])
humedad_optima = fuzz.trimf(humedad, [30, 40, 70])
humedad_alta = fuzz.trimf(humedad, [70, 80, 100])

#funciones de pertenencia para los nutrientes
nutrientes_bajos = fuzz.trimf(nutrientes, [0, 20, 40])
nutrientes_optimos = fuzz.trimf(nutrientes, [30, 40, 60])
nutrientes_altos = fuzz.trimf(nutrientes, [50, 80, 100])

#funciones de pertenencia para la fertilización
fertilizacion_baja = fuzz.trimf(fertilizacion, [0, 15, 30])
fertilizacion_optima = fuzz.trimf(fertilizacion, [30, 40, 70 ])
fertilizacion_alta = fuzz.trimf(fertilizacion, [70, 80, 100])

fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(10, 8))

ax0.plot(humedad, humedad_baja, "b", label="Humedad Baja")
ax0.plot(humedad, humedad_optima, "g", label="Humedad Óptima")
ax0.plot(humedad, humedad_alta, "r", label="Humedad Alta")
ax0.set_title("Funciones de pertenencia: Humedad")
ax0.grid(True)
ax0.legend()
ax0.set_xlim(0, 100)
ax0.set_ylim(0, 1)

ax1.plot(nutrientes, nutrientes_bajos, "b", label="Nutrientes Bajos")
ax1.plot(nutrientes, nutrientes_optimos, "g", label="Nutrientes Óptimos")
ax1.plot(nutrientes, nutrientes_altos, "r", label="Nutrientes Altos")
ax1.set_title("Funciones de pertenencia: Nutrientes")
ax1.grid(True)
ax1.legend()
ax1.set_xlim(0, 100)
ax1.set_ylim(0, 1)

ax2.plot(fertilizacion, fertilizacion_baja, "b", label="Fertilización Baja")
ax2.plot(fertilizacion, fertilizacion_optima, "g", label="Fertilización Óptima")
ax2.plot(fertilizacion, fertilizacion_alta, "r", label="Fertilización Alta")
ax2.set_title("Funciones de pertenencia: Fertilización")
ax2.grid(True)
ax2.legend()
ax2.set_xlim(0, 100)
ax2.set_ylim(0, 1)

                
plt.tight_layout()
plt.show()

while True:
    try:
        humedad_usuario = int(input("Ingrese la humedad del suelo(0-100): "))
        nutrientes_usuario = int(input("Ingrese la cantidad de nutrientes(0-100): "))
        if humedad_usuario == 0 or nutrientes_usuario == 0:
            break
            
        else:
            if 0 < humedad_usuario <= 100 and 0 < nutrientes_usuario <= 100:

                #grados de pertenencia para humedad
                humedad_baja = fuzz.interp_membership(humedad, humedad_baja, humedad_usuario)
                humedad_optima = fuzz.interp_membership(humedad, humedad_optima, humedad_usuario)
                humedad_alta = fuzz.interp_membership(humedad, humedad_alta, humedad_usuario)

                #grados de pertenencia para nutrientes
                nutrientes_bajos = fuzz.interp_membership(nutrientes, nutrientes_bajos, nutrientes_usuario)
                nutrientes_optimos = fuzz.interp_membership(nutrientes, nutrientes_optimos, nutrientes_usuario)
                nutrientes_altos = fuzz.interp_membership(nutrientes, nutrientes_altos, nutrientes_usuario)
                
                # Regla 1: Si humedad es baja O nutrientes son bajos -> fertilización alta
                regla1 = np.fmax(humedad_baja, nutrientes_bajos)

                # Regla 2: Si humedad es óptima Y nutrientes óptimos -> fertilización óptima
                regla2 = np.fmin(humedad_optima, nutrientes_optimos)

                # Regla 3: Si humedad alta O nutrientes altos -> fertilización baja
                regla3 = np.fmax(humedad_alta, nutrientes_altos)
                
                activacion_baja = np.fmin(regla3, fertilizacion_baja)
                activacion_media = np.fmin(regla2, fertilizacion_optima)
                activacion_alta = np.fmin(regla1, fertilizacion_alta)

                agregado = np.fmax(activacion_baja, np.fmax(activacion_media, activacion_alta))
                resultado = fuzz.defuzz(fertilizacion, agregado, 'centroid')
                print(f"Resultado de la fertilización: {resultado:.2f}")

                plt.figure(figsize=(8,4))
                plt.plot(fertilizacion, fertilizacion_baja, 'b', linestyle='--')
                plt.plot(fertilizacion, fertilizacion_optima, 'g', linestyle='--')
                plt.plot(fertilizacion, fertilizacion_alta, 'r', linestyle='--')
                plt.fill_between(fertilizacion, 0, agregado, facecolor='Orange', alpha=0.7)
                plt.plot([resultado, resultado], [0, 1], 'k', linewidth=2, alpha=0.7)
                plt.title('Nivel de Fertilización Recomendado')
                plt.grid(True)
                plt.xlim(0, 100)
                plt.ylim(0, 1)

                plt.show()
                plt.tight_layout()
            else:
                print("Escriba los ingresos dentro del rango establecido.")
    except ValueError:
        print("Ingrese un número válido")