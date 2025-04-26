import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

temperatura = np.arange(0, 41, 1)
humedad = np.arange(0, 101, 1)
prob_lluvia = np.arange(0, 101, 1)


#definimos las funciones de pertenencia para la temperatura
frio = fuzz.trimf(temperatura, [0, 10, 20])
templado = fuzz.trimf(temperatura, [15, 25, 35])
caliente = fuzz.trimf(temperatura, [30, 40, 40])

#funciones de pertenencia para la humedad
humedad_baja = fuzz.trimf(humedad, [0, 25, 50])
humedad_media = fuzz.trimf(humedad, [30, 50, 70])
humedad_alta = fuzz.trimf(humedad, [60, 80, 100])

#funciones de pertenencia para la probabilidad de lluvia
prob_baja = fuzz.trimf(prob_lluvia, [0, 25, 50])
prob_media = fuzz.trimf(prob_lluvia, [30, 50, 70])
prob_alta = fuzz.trimf(prob_lluvia, [60, 80, 100])

plt.figure(figsize=(10, 8))

#temperatura
plt.subplot(3, 1, 1)
plt.plot(temperatura, frio, 'b', linewidth=2, label='Frío')
plt.plot(temperatura, templado, 'g', linewidth=2, label='Templado')
plt.plot(temperatura, caliente, 'r', linewidth=2, label='Caliente')

plt.title('Temperatura, sistema difuso')

plt.xlabel('Temperatura (°C)')
plt.ylabel('Grado de pertenencia')
plt.legend()
plt.grid(True)

#humedad
plt.subplot(3, 1, 2)
plt.plot(humedad, humedad_baja, 'b', linewidth=2, label='Humedad Baja')
plt.plot(humedad, humedad_media, 'g', linewidth=2, label='Humedad Media')
plt.plot(humedad, humedad_alta, 'r', linewidth=2, label='Humedad Alta')
plt.title('Funciones de membresía - Humedad')
plt.xlabel('Humedad (%)')
plt.ylabel('Grado de pertenencia')
plt.legend()
plt.grid(True)

#probabilidad de lluvia
plt.subplot(3, 1, 3)
plt.plot(prob_lluvia, prob_baja, 'b', linewidth=2, label='Lluvia Baja')
plt.plot(prob_lluvia, prob_media, 'g', linewidth=2, label='Lluvia Media')
plt.plot(prob_lluvia, prob_alta, 'r', linewidth=2, label='Lluvia Alta')
plt.title('Funciones de membresía - Probabilidad de Lluvia')
plt.xlabel('Probabilidad de Lluvia (%)')
plt.ylabel('Grado de pertenencia')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()