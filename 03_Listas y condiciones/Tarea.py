def clasificar_nota(nota):
    if nota >= 90:
        return "Excelente"
    elif nota >= 75:
        return "Bueno"
    elif nota >= 60:
        return "Suficiente"
    else:
        return "Reprobado"
    
def reporte_salon(lista_notas):
    suma = sum(lista_notas)
    total = len(lista_notas)
    print(f"Promedio del salón (desde archivo): {suma/total:.2f}")
    print(f"{max(lista_notas)}")
    print(f"{min(lista_notas)}")
    aprovados = [nota for nota in lista_notas if nota >= 70]
    print(f"La cantidad de aprovados fue: {len(aprovados)}")
    reprobados = [nota for nota in lista_notas if nota < 70]
    print(f"La cantidad de reprobados fue: {len(reprobados)}")


lista_notas=[]
with open("notas_ejemplo.csv") as notas:
    next(notas)
    for linea in notas:
        datos = linea.strip().split(",")
        nota = float(datos[1])
        nombre = datos[0]
        lista_notas.append(nota)
        print(f"{nombre}: {datos[1]} → {clasificar_nota(nota)} ")
reporte_salon(lista_notas)



