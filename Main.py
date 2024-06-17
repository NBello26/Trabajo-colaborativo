import Funciones as funcion

#Coleccion para guardar los trabajadores
trabajadores= []
#Tipos de Cargos
cargos = ["CEO", "Desarrollador", "Analista de Datos"]
usuarios = {
    "Nicolas" : "123",
    "Martin"  : "1234",
    "Benja"   : "12345",
    "Calfun"  : "12"
};
flagmenu = True;
flagLogin = True;
while flagLogin:
    login = funcion.login(usuarios);
    if login == True:
        flagLogin = False;

while flagmenu:
    print("Bienvenido a ProgramDuoc\n1.- Registrar usuarios\n2.- Listar todos los trabajadores\n3.- Imprimir planilla de sueldos\n4.- Salir del programa\n");
    opcion = input("Ingrese la opcion que desea: ");
    if opcion == "1":
        trabajadores = funcion.registrar_trabajador(trabajadores,cargos);
    elif opcion == "2":
        print("\nListando todos los trabajadores...\n");
        funcion.listar_trabajadores(trabajadores);
    elif opcion == "3":
        print("\nImprimiendo planilla...\n")
        funcion.imprimir_planilla(trabajadores);
    elif opcion == "4":
        print("\nSaliendo del programa, nos vemos en otra ocación");
        flagmenu == False;
    else:
        print("\nOpción ingresada incorrecta. Intentelo nuevamente.\n");