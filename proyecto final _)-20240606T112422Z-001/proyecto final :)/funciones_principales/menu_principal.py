import datos
import menu_ges.gestion_camper as opciones_camper
import menu_ges.gestion_trainer as opciones_trainers
import menu_ges.gestion_coordinador as opciones_coordinador
import menu_ges.gestion_coordinador as opciones_coordinador 
import menu_coordi.materias as opciones_coordinador_materias
import menu_coordi.rutas as opciones_coordinador_rutas
import menu_coordi.matriculas as opciones_coordinador_matriculas



def menu_():
    datos.cargar_usuario()
    while True:
        print("***********************************************")
        print("Bienvenido a campuslands:")
        print("1. Ingresar como camper")
        print("2. Ingresar como trainer")
        print("3. Ingresar como coordinador")
        print("4. salir")
        print("***********************************************")
        opcion=0
        try:
            opcion=int(input("ingrese la opcion a escoger"))
        except Exception:
            print("opcion invalida, por favor digite una de las opciones en el menu")
        if opcion == 1:
            menu_camper()
        elif opcion == 2:
            menu_trainer()
        elif opcion == 3:
            menu_coordinador()
        elif opcion == 4:
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("opcion invalida, por favor digite una de las opciones en el menu")




        #definiciones de los menus (camper,trainer,coordinador)
        #opciones camper
            def menu_camper():
                while True:
                    print("***********************************************")
                    print(" menu camper")
                    print("1.Mostrar los campers")
                    print("2.Registrar un camper nuevo")
                    print("3.Editar los datos del camper")
                    print("4.eliminar camper")
                    print("5.regresar al menu principal")
                    print("***********************************************")
                    try:
                        opcion=int(input("ingrese la opcion deseada"))
                    except ValueError:
                        print("opcion invalida, por favor ingrese una opcion valida")
                        continue
                    if opcion == 1:
                        opciones_camper.mostrar_campers()
                    elif opcion == 2:
                        opciones_camper.registros_campers()
                    elif opcion == 3:
                        opciones_camper.actualiza_campers()
                    elif opcion == 4:
                        opciones_camper.eliminar_campers()
                    elif opcion ==5:
                        break
                    else:
                        print("opcion incorrecta, por favor ingrese una de las opciones mostradas")

    #opciones trainer
            def menu_trainer():
                while True:
                    print("***********************************************")
                    print(" menu trainer")
                    print("1.Mostrar los trainer")
                    print("2.Registrar un trainer")
                    print("3.Editar los datos del trainer")
                    print("4.regresar al menu principal")
                    print("***********************************************")
                    try:
                        opcion=int(input("ingrese la opcion deseada"))
                    except ValueError:
                        print("opcion invalida, por favor ingrese una opcion valida")
                        continue
                    if opcion == 1:
                        opciones_trainers.mostrar_trainers()
                    elif opcion == 2:
                        opciones_trainers.registros_trainer()
                    elif opcion == 3:
                        opciones_trainers.actualizar_trainer()
                    elif opcion == 4:
                        break
                    else:
                        print("opcion incorrecta,por favor ingrese una de las opciones mostradas")
            def menu_coordinador():
                while True:
                    print("***********************************************")
                    print(" menu coordinador :)")
                    print("1.menu materias-coordinador")
                    print("2.menu rutas-coordinador")
                    print("3.menu matriculas-coordinador")
                    print("4. menu notas-coordinador")
                    print("5.regresar al menu principal")
                    print("***********************************************")
                    try:
                        opcion=int(input("ingrese la opcion deseada"))
                    except ValueError:
                        print("opcion invalida, por favor ingrese una opcion valida")
                        continue
                    if opcion == 1:
                        menu_materias()
                    elif opcion == 2:
                        menu_rutas()
                    elif opcion == 3:
                        menu_matriculas()
                    elif opcion == 4:
                        menu_notas()
                    elif opcion ==5:
                        break
                    else:
                        print("opcion incorrecta, por favor ingrese una de las opciones mostradas")

    #menu completo de coordinador(rutas,materias,matriculas,notas)

def menu_materias():
                while True:
                    print("***********************************************")
                    print(" menu materias-coordinador")
                    print("1.Mostrar materias registradas")
                    print("2.Registrar una materia nueva")
                    print("3.Editar una materia existente")
                    print("4.eliminar materia")
                    print("5.regresar al menu principal")
                    print("***********************************************")
                    try:
                        opcion=int(input("ingrese la opcion deseada"))
                    except ValueError:
                        print("opcion invalida, por favor ingrese una opcion valida")
                        continue
                    if opcion == 1:
                        opciones_coordinador_materias.mostrar_materia()
                    elif opcion == 2:
                        opciones_coordinador_materias.registrar_materias()
                    elif opcion == 3:
                        opciones_coordinador_materias.actualizar_materia()
                    elif opcion == 4:
                        opciones_coordinador_materias.eliminar_materia()
                    elif opcion ==5:
                        break
                    else:
                        print("opcion incorrecta, por favor ingrese una de las opciones mostradas")

def menu_rutas():
                while True:
                    print("***********************************************")
                    print(" menu rutas-coordinador")
                    print("1.Mostrar rutas registradas")
                    print("2.Registrar una nueva ruta")
                    print("3.Editar una ruta existente")
                    print("4.eliminar ruta")
                    print("5.regresar al menu principal")
                    print("***********************************************")
                    try:
                        opcion=int(input("ingrese la opcion deseada"))
                    except ValueError:
                        print("opcion invalida, por favor ingrese una opcion valida")
                        continue
                    if opcion == 1:
                        opciones_coordinador_rutas.mostrar_rutas()
                    elif opcion == 2:
                        opciones_coordinador_rutas.registrar_rutas()
                    elif opcion == 3:
                        opciones_coordinador_rutas.actualizar_rutas()
                    elif opcion == 4:
                        opciones_coordinador_rutas.eliminar_rutas()
                    elif opcion ==5:
                        break
                    else:
                        print("opcion incorrecta, por favor ingrese una de las opciones mostradas")

def menu_matriculas():
                while True:
                    print("***********************************************")
                    print(" menu matriculas-coordinador")
                    print("1.Mostrar matriculas registradas")
                    print("2.Registrar una nueva matricula")
                    print("3.Editar una matriucla existente")
                    print("4.eliminar matricula")
                    print("5.regresar al menu principal")
                    print("***********************************************")
                    try:
                        opcion=int(input("ingrese la opcion deseada"))
                    except ValueError:
                        print("opcion invalida, por favor ingrese una opcion valida")
                        continue
                    if opcion == 1:
                        opciones_coordinador_matriculas.mostrar_matriculas()
                    elif opcion == 2:
                        opciones_coordinador_matriculas.registro_matriculas()
                    elif opcion == 3:
                        opciones_coordinador_matriculas.editar_matriculas()
                    elif opcion == 4:
                        opciones_coordinador_matriculas.eliminar_matriculas()
                    elif opcion ==5:
                        break
                    else:
                        print("opcion incorrecta, por favor ingrese una de las opciones mostradas")
        
def menu_notas():
                while True:
                    print("***********************************************")
                    print(" menu notas-coordinador")
                    print("1.Mostrar notas registradas")
                    print("2.Registrar una nota nueva")
                    print("3.Editar una nota existente")
                    print("4.eliminar nota")
                    print("5.regresar al menu principal")
                    print("***********************************************")
                    try:
                        opcion=int(input("ingrese la opcion deseada"))
                    except ValueError:
                        print("opcion invalida, por favor ingrese una opcion valida")
                        continue
                    if opcion == 1:
                        opciones_coordinador.mostrar_notas_registradas()
                    if opcion == 2:
                        opciones_coordinador.registro_de_notas_nuevo()
                    if opcion == 3:
                        opciones_coordinador.editar_notas_registradas()
                    if opcion == 4:
                        opciones_coordinador.eliminar_notas_registradas()

                    elif opcion ==5:
                        break
                    else:
                        print("opcion incorrecta, por favor ingrese una de las opciones mostradas")


                






