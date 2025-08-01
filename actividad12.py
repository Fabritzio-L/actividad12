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
        except ValueError:
            print("Error: ingrese valores validos.")
            for j in range(cantidad_notas):
                nota= int(input("Ingrese la nota: "))
                notas.append(nota)
                for nota in notas:
                    promedio = sum(nota)/len(nota)
    except ValueError:
        print("Error: ingrese valores validos.")
    except ZeroDivisionError:
        print("Error: no se puede calcular promedio sin notas ingresadas.")
    except TypeError:
        print("Error: No se pueden combinar diferentes tipos de datos")
    except Exception as e:
        print("Se produjo un error inesperado:", e)
    else:
        for estudiante in estudiantes:
            print(estudiante)
            print(promedio)
    finally:
        print("Fin del proceso")