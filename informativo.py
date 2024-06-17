
#Coleccion para guardar los trabajadores
trabajadores= []

#Tipos de Cargos
cargos = ["CEO", "Desarrollador", "Analista de Datos"]


def registrar_trabajador():
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
    
    print("Trabajador exitosamente registrado")