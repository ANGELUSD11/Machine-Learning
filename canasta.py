import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Generación de datos sintéticos
# -------------------------------
np.random.seed(100)

# Cantidad de productos comprados (entre 5 y 50)
productos = np.random.randint(5, 50, 50)

# Simulación del gasto total en pesos colombianos (COP)
# Se asume un costo promedio de 8,000 COP por producto con variación aleatoria
gasto = productos * 8000 + np.random.randint(-10000, 10000, 50)

# Crear un DataFrame con pandas
df = pd.DataFrame({'Cantidad de Productos': productos, 'Gasto Total (COP)': gasto})

# -------------------------------------
# Visualización de los datos simulados
# -------------------------------------
plt.scatter(df['Cantidad de Productos'], df['Gasto Total (COP)'], color='blue', label="Datos reales")
plt.xlabel('Cantidad de Productos')
plt.ylabel('Gasto Total (COP)')
plt.title('Relación entre la Cantidad de Productos y el Gasto en Mercado')
plt.grid()
plt.legend()
plt.show()

# -------------------------------------
# Implementación de la regresión lineal
# -------------------------------------
X = df['Cantidad de Productos'].values  # Variable independiente (cantidad de productos)
y = df['Gasto Total (COP)'].values  # Variable dependiente (dinero gastado)

# Cálculo de la pendiente (m) y la intersección (b) usando mínimos cuadrados
m = (np.mean(X*y) - np.mean(X) * np.mean(y)) / (np.mean(X**2) - np.mean(X)**2)
b = np.mean(y) - m * np.mean(X)

# Imprimir la ecuación de la regresión
print(f"Ecuación de la regresión: Gasto = {m:.2f} * Cantidad de Productos + {b:.2f}")

# -------------------------------------
# Función para predecir el gasto en mercado
# -------------------------------------
def predict(cantidad_productos):
    """Devuelve el gasto estimado en COP para una cantidad de productos dada."""
    return m * cantidad_productos + b

# -------------------------------------
# Graficar la regresión lineal
# -------------------------------------
plt.scatter(df['Cantidad de Productos'], df['Gasto Total (COP)'], color='blue', label="Datos reales")
plt.plot(df['Cantidad de Productos'], predict(df['Cantidad de Productos']), color='red', label="Regresión Lineal")
plt.xlabel('Cantidad de Productos')
plt.ylabel('Gasto Total (COP)')
plt.title('Predicción del Gasto en Mercado')
plt.grid()
plt.legend()
plt.show()

# -------------------------------------
# Predicción del gasto en una compra específica
# -------------------------------------
cantidad_nueva = 20  # Ejemplo: Comprar 20 productos
gasto_predicho = predict(cantidad_nueva)
print(f"El gasto estimado al comprar {cantidad_nueva} productos en el mercado es de {gasto_predicho:.2f} COP.")
