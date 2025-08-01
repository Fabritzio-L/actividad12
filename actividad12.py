estudiantes={}
while True:
    try:
        cantidad_estudiantes= int(input("¿Cuantos estudiantes desea ingresar: "))
        break
    except ValueError:
            print("Error: ingrese valores validos.")
for i in range(cantidad_estudiantes):
    nombre= input("Ingrese nombre del estudiante: ")
    notas=[]
    while True:
        try:
            cantidad_notas= int(input("¿Cuantas notas desea ingresar?: "))
            break
        except ValueError:
            print("Error: ingrese un numero entero.")
    for j in range(cantidad_notas):
        while True:
            try:
                nota= int(input("Ingrese la nota: "))
                notas.append(nota)
                break
            except ValueError:
                print("Error: ingrese un numero entero")
    try:
        promedio = sum(notas)/cantidad_notas
        estudiantes[nombre]=promedio
    except ZeroDivisionError:
        print("Error: No se puede calcular el promedio sin ninguna nota.")
    except TypeError:
        print("Error: Operacion invalida entre distinto tipos de datos.")
    except Exception as e:
        print("Error inesperado: ",e)
    else:
        print("Notas registradas")
    finally:
        print("Registro de estudiante finalizado")
print("\nPromedio de estudiantes")
for nombre, promedio in estudiantes.items():
    print(f"{nombre}: {promedio:.2f}")