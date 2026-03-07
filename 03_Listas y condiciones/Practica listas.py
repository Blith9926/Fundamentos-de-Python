# Crea una lista llamada `tareas` con estas 3 tareas iniciales:
# "Estudiar Python", "Hacer ejercicio", "Leer un libro"

tareas = ["Estudiar Python", "Hacer ejercicio", "Leer un libro"]

# 1. AGREGAR: Añade "Comprar comida" al final de la lista.
tareas.append("Comprar comida")

# 2. INSERTAR: Inserta "Llamar al médico" en la posición 1.
tareas.insert(1, "Llamar al medico")

# 3. MOSTRAR CANTIDAD: Imprime cuántas tareas hay en total.
print(len(tareas))
print(tareas)
# 4. ORDENAR: Ordena las tareas alfabéticamente e imprímelas.
tareas.sort()
print(tareas)
# 5. ELIMINAR: Elimina "Hacer ejercicio" de la lista.
tareas.remove("Hacer ejercicio")

# 6. EXTRAER: Extrae (pop) la última tarea y guárdala en una
#    variable llamada `ultima`. Imprímela con el mensaje:
#    "Tarea removida: ..."
print(f"Tarea removida: {tareas.pop(3)}")
print(tareas)
# 7. BUSCAR: Verifica si "Leer un libro" sigue en la lista.
#    Imprime True o False.
if "Leer un libro" in tareas:
    print("Si está")
else:
    print("No está")

# 8. SLICE: Imprime solo las primeras 2 tareas de la lista final.*

print(tareas)