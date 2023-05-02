#Datos de los integrantes
Integrantes = ["Félix","Marilyn","Ivan","Alejandro","Sonia","Carlos"]
Nombres = ["Félix Mauricio","Marilyn Alexandra","Ivan Anderson","Alejandro Adonay","Sonia Elizabeth","Carlos Ernesto"]
Apellidos = ["Palacios Tejada","Menjivar Fuentes","Membreño Guardado","Cañas Hernández","Abrego Núñez","Landaverde Quintanilla"]
Sexo = ["Masculino","Femenino"]
Edad = [17,18,19]
Departamento = ["San Salvador","Chalatenango","Cuscatlán"]
Municipio = ["El Paisnal","La laguna","Guancora","Suchitoto","Dulce Nombre de María","San Luis del Carmen"]
Direccion = ["Carretera troncal del Norte Km 43/2, Potrero Grande, El Paisnal","Primer callejon  a la derecha","Sector 1","Caserío el cereto","Barrio El Calvario","Chalatenango, San Luis del Carmen"]

#Definir la función
def EjecutarPrograma():
    Inicio = True
    z = 1

    while Integrantes:

        #Reinicio del programa
        if z == 2:
            PInicio = input("\n¿Desea reiniciar el progama? -> ").lower()

            if PInicio == "Si".lower():
                Inicio = True

            elif PInicio == "no".lower():
                break

            else:
                print("\n\t~~~ Opción no válida ~~~")            

        #Programa
        while Inicio == True:
            y = 0
            print("\n*+*+*+*+*+*+*+*+*+*+*+*+*+")
            print("*+Bienvenido al programa*+")
            print("*+*+*+*+*+*+*+*+*+*+*+*+*+\n")
            print("""En este programa debera seleccionar un nombre de los apareceran \ny se le mostrarran los datos pertenecientes al individuo seleccionado\n""")

            while y < 5 and Inicio == True:

                #Selección del integrante
                print("\tIntegrantes\n")

                x = 0
                for i in range(6):
                    print(f"\t{x + 1}- {Integrantes[x]}")
                    x += 1
                
                Select = input("\nSeleccione un nombre -> ").lower()
                
                #Resultados de la selección
                if Select == "Felix".lower() or Select == "Félix".lower() or Select == "1":
                    print(f"\n\tDatos del integrante:\n\n\tNombres: {Nombres[0]}\n\tApellidos: {Apellidos[0]}\n\tSexo: {Sexo[0]}\n\tEdad: {Edad[0]}\n\tDepartamento: {Departamento[0]}\n\tMunicipio: {Municipio[0]}\n\tDirección: {Direccion[0]}")
                    Inicio = False
                    z = 2

                elif Select == "Marilyn".lower() or Select == "2":
                    print(f"\n\tDatos del integrante:\n\n\tNombres: {Nombres[1]}\n\tApellidos: {Apellidos[1]}\n\tSexo: {Sexo[1]}\n\tEdad: {Edad[1]}\n\tDepartamento: {Departamento[1]}\n\tMunicipio: {Municipio[1]}\n\tDirección: {Direccion[1]}")
                    Inicio = False
                    z = 2

                elif Select == "Ivan".lower() or Select == "3":
                    print(f"\n\tDatos del integrante:\n\n\tNombres: {Nombres[2]}\n\tApellidos: {Apellidos[2]}\n\tSexo: {Sexo[0]}\n\tEdad: {Edad[1]}\n\tDepartamento: {Departamento[1]}\n\tMunicipio: {Municipio[2]}\n\tDirección: {Direccion[2]}")
                    Inicio = False
                    z = 2

                elif Select == "Alejandro".lower() or Select == "4":
                    print(f"\n\tDatos del integrante:\n\n\tNombres: {Nombres[3]}\n\tApellidos: {Apellidos[3]}\n\tSexo: {Sexo[0]}\n\tEdad: {Edad[1]}\n\tDepartamento: {Departamento[2]}\n\tMunicipio: {Municipio[3]}\n\tDirección: {Direccion[3]}")
                    Inicio = False
                    z = 2

                elif Select == "Sonia".lower() or Select == "5":
                    print(f"\n\tDatos del integrante:\n\n\tNombres: {Nombres[4]}\n\tApellidos: {Apellidos[4]}\n\tSexo: {Sexo[1]}\n\tEdad: {Edad[2]}\n\tDepartamento: {Departamento[1]}\n\tMunicipio: {Municipio[4]}\n\tDirección: {Direccion[4]}")
                    Inicio = False
                    z = 2

                elif Select == "Carlos".lower() or Select == "6":
                    print(f"\n\tDatos del integrante:\n\n\tNombres: {Nombres[5]}\n\tApellidos: {Apellidos[5]}\n\tSexo: {Sexo[0]}\n\tEdad: {Edad[0]}\n\tDepartamento: {Departamento[1]}\n\tMunicipio: {Municipio[5]}\n\tDirección: {Direccion[5]}")
                    Inicio = False
                    z = 2

                #Contador de intentos fallidos
                else:
                    if y == 4:
                        print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("~~ Demasiados intentos fallidos ~~")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                        Inicio = False
                        z = 2
                    
                    else:
                        y += 1
                        z = 2
                        print("\n~~~ Dato no válido, vuelva a intentarlo ~~~\n")

#Definir el inicio del programa
while Integrantes:
    PInicio = input("\n¿Desea iniciar el progama? -> ").lower()

    if PInicio == "Si".lower():
        EjecutarPrograma()
        break

    elif PInicio == "no".lower():
        break

    else:
        print("\n\t~~~ Opción no válida ~~~")            

print("\nFin del programa")