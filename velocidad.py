import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# 1. Universo de discurso
temperatura = np.arange(0, 41, 1)         # Entrada: 0 a 40 °C
velocidad = np.arange(0, 101, 1)          # Salida: 0 a 100 % de velocidad

# 2. Funciones de membresía - Entrada
temp_frio = fuzz.trimf(temperatura, [0, 0, 20])
temp_templado = fuzz.trimf(temperatura, [15, 25, 35])
temp_caliente = fuzz.trimf(temperatura, [30, 40, 40])

# 3. Funciones de membresía - Salida
vel_lenta = fuzz.trimf(velocidad, [0, 0, 50])
vel_media = fuzz.trimf(velocidad, [30, 50, 70])
vel_rapida = fuzz.trimf(velocidad, [60, 100, 100])

# 4. Visualización
fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(10, 8))

ax0.plot(temperatura, temp_frio, 'b', label='Frío')
ax0.plot(temperatura, temp_templado, 'g', label='Templado')
ax0.plot(temperatura, temp_caliente, 'r', label='Caliente')
ax0.set_title('Funciones de membresía: Temperatura')
ax0.legend()
ax0.grid(True)

ax1.plot(velocidad, vel_lenta, 'b', label='Lenta')
ax1.plot(velocidad, vel_media, 'g', label='Media')
ax1.plot(velocidad, vel_rapida, 'r', label='Rápida')
ax1.set_title('Funciones de membresía: Velocidad del Ventilador')
ax1.legend()
ax1.grid(True)

plt.tight_layout()
plt.show()