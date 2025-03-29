def clasificar_residuo(residuo):
    residuo = residuo.lower().strip()

    # Diccionario con los tipos de residuos y sus colores de contenedor
    residuos_info = {
        "aprovechable": {
            "residuos": ["plástico", "cartón", "vidrio", "papel", "metales"],
            "color": "blanco"
        },
        "no aprovechable": {
            "residuos": ["papel higiénico", "servilletas", "cartones contaminados", "papeles metalizados"],
            "color": "negro"
        },
        "peligroso": {
            "residuos": ["grasas", "aceites", "combustibles"],
            "color": "rojo"
        }
    }

    # Buscar a qué tipo pertenece el residuo
    for clasificacion, info in residuos_info.items():
        # Comprobar si el residuo ingresado está en la lista de residuos
        if residuo in info["residuos"]: #info accede a las listas dentro de las claves (accede a los valores)
            return f"El residuo '{residuo}' es de tipo '{clasificacion}'. Debe depositarse en el contenedor de color '{info['color']}'."
    
    # Si no se encuentra, mostrar un mensaje
    return f"No se encontró la clasificación de este residuo '{residuo}'. Intenta con otro material."

print("Clasificador de residuos")
print("-----------------------------")

try:
    residuo = input("Ingresa el tipo de residuo (ejemplo: plástico, servilleta, aceite, etc.): ")
    
    resultado = clasificar_residuo(residuo)
    print(f"\n{resultado}")

except Exception as e:
    print(f"\nError: {e}")