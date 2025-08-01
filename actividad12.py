estudiantes={}
try:
    cantidad_estudiantes= int(input("¿Cuantos estudiantes desea ingresar: "))
except ValueError:
        print("Error: ingrese valores validos.")
else:
    for i in range(cantidad_estudiantes):
        nombre= input("Ingrese nombre del estudiante: ")
        notas=[]
        try:
            cantidad_notas= int(input("¿Cuantas notas desea ingresar?: "))
            for j in range(cantidad_notas):
                while True:
                    try:
                        nota= int(input("Ingrese la nota: "))
                        notas.append(nota)
                        break
                    except ZeroDivisionError:
                        print("Error: no se puede calcular promedio sin notas ingresadas.")
            promedio = sum(notas)/cantidad_notas
            estudiantes[nombre]=promedio
        except ValueError:
            print("Error: ingrese un numero entero")
        except ZeroDivisionError:
            print("Error: No se puede calcular el promedio sin ninguna nota.")
        except TypeError:
            print("Error: Operacion invalida entre distinto tipos de datos.")
        except Exception as e:
            print("Error inesperado: ",e)
        finally:
            print("Registro de estudiante finalizado")
finally:
    print()