def login(usuarios):
    # Pedir al usuario que ingrese su nombre de usuario y contraseña
    usuario = input("Ingrese su nombre de usuario: ");
    clave = input("Ingrese su contraseña: ");

    # Verificar si el usuario existe en el diccionario y si la contraseña es correcta
    if usuario in usuarios and usuarios[usuario] == clave:
        print("¡Bienvenido,", usuario, "!");
        return True;
    else:
        print("Nombre de usuario o contraseña incorrectos. Por favor, inténtelo de nuevo.");
        return False;

def registrar_trabajador(trabajadores,cargos):
    print("Registrar Trabajador")
    flag =True
    while flag:
        nombre_apellido = input("Ingrese su Nombre y Apellido:")
        cargo = input("Ingrese su cargo (CEO, Desarrollador o Analista de Datos):")
        if cargo not in cargos:
            print("Cargo no válido.")
        else:
            flag = False;
    sueldobruto = float(input("Ingrese su sueldo bruto:"))
    #Calcular descuentos
    desc_salud = sueldobruto * 0.07;
    desc_afp = sueldobruto * 0.12;
    desc_total = desc_afp + desc_salud;
    sueldo_liquido = sueldobruto - desc_total;
    #Registrar Trabajadores en la coleccion
    trabajadores.append(
        [nombre_apellido,
        cargo,
        sueldobruto,
        desc_salud,
        desc_afp,
        sueldo_liquido]
    )
    return trabajadores

def imprimir_planilla(lista):
    preguntascargo = True;
    while preguntascargo:
        pregunta_cargo = input("Desea imprimir todos los empleados?(Si/No): ");
        if pregunta_cargo.lower() == "si":
            cargo = "TODOS";
            preguntascargo = False;
        elif pregunta_cargo.lower() == "no":
            cargo = input("¿Qué cargo desea imprimir?: ");
            preguntascargo = False;
        else:
            print("Opción ingresada incorrecta, intentelo nuevamente");
    imprimir_sueldos(lista,cargo);

def imprimir_sueldos(lista,cargo):
    with open('Planilla_Sueldos.txt', 'w', encoding= "utf-8") as archivo:
        archivo.write("Trabajador - Cargo - Sueldo Bruto  - Desc. Salud Desc. - AFP Líquido a pagar\n");
        for i in lista:
            if cargo == "TODOS":
                archivo.write(f"{i[0]} - {i[1]} - {i[2]} - {i[3]} - {i[4]}\n");
            else:
                if cargo.upper() == i[1]:
                    archivo.write(f"{i[0]} - {i[1]} - {i[2]} - {i[3]} - {i[4]}\n");

def listar_trabajadores(lista):
    #Listar todos los trabajadores
    lista1 = ["Trabajador","Cargo","Sueldo Bruto","Desc. Salud", "Desc. AFP", "Líquido a pagar"]
    print(lista1)
    print(lista)