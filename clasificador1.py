import tkinter as tk
from tkinter import messagebox

def clasificar_residuo(residuo):
    residuo = residuo.lower().strip()

    residuos_info = {
        "aprovechable": {
            "residuos": ["plástico", "plastico", "cartón", "carton", "vidrio", "papel", "metales", "metal"],
            "color": "blanco"
        },
        "no aprovechable": {
            "residuos": ["papel higiénico", "servilletas", "servilleta", "cartones contaminados", "papeles metalizados"],
            "color": "negro"
        },
        "peligroso": {
            "residuos": ["grasa", "grasas", "aceite", "aceites", "combustible", "combustibles"],
            "color": "rojo"
        },
        "electrónico": {
            "residuos": ["batería", "baterías", "celular", "computadora", "cargador", "electrodoméstico"],
            "color": "gris"
        },
        "especial reciclaje": {
            "residuos": ["pilas", "bombillo", "toner", "medicamentos vencidos", "jeringas"],
            "color": "naranja"
        }
    }

    for clasificacion, info in residuos_info.items():
        for r in info["residuos"]:
            if r in residuo:
                return f"El residuo '{residuo}' es de tipo '{clasificacion}'. Debe depositarse en el contenedor de color '{info['color']}'."

    sugerencias = []
    for clasificacion, info in residuos_info.items():
        for r in info["residuos"]:
            if any(word in r for word in residuo.split()):
                sugerencias.append(r)

    if sugerencias:
        sugerencias_str = ", ".join(set(sugerencias))
        return f"No se encontró la clasificación exacta de '{residuo}'. ¿Quisiste decir: {sugerencias_str}?"

    return f"No se encontró la clasificación de este residuo '{residuo}'. Intenta con otro término o revisa la ortografía."


def mostrar_resultado():
    residuo = entrada.get()
    resultado = clasificar_residuo(residuo)
    messagebox.showinfo("Resultado", resultado)


if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.title("Clasificador de Residuos")

    etiqueta = tk.Label(ventana, text="Ingresa el tipo de residuo:")
    etiqueta.pack(pady=5)

    entrada = tk.Entry(ventana, width=40)
    entrada.pack(pady=5)

    boton = tk.Button(ventana, text="Clasificar", command=mostrar_resultado)
    boton.pack(pady=10)

    ventana.mainloop()


# Pruebas unitarias
if __name__ == "__test__":
    def test_clasificar_residuo():
        assert "blanco" in clasificar_residuo("plastico")
        assert "negro" in clasificar_residuo("servilleta")
        assert "rojo" in clasificar_residuo("aceite")
        assert "gris" in clasificar_residuo("batería")
        assert "naranja" in clasificar_residuo("pilas")
        assert "clasificación" in clasificar_residuo("desconocido")
    
    test_clasificar_residuo()
    print("Todas las pruebas pasaron.")
