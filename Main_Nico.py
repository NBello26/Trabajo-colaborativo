import Funciones_Nico as funcion

lista = [["Homero Simpson","CEO", 1000000, 70000, 120000, 810000],
         ["Bart Simpson","GERENTE", 1000000, 70000, 120000, 810000],
         ["Lisa Simpson","GERENTE GENERAL", 1000000, 70000, 120000, 810000],
         ["Maggie Simpson","SECRETARIA", 1000000, 70000, 120000, 810000],
         ["Nico Simpson","GERENTE", 1000000, 70000, 120000, 810000],
         ["Martin Simpson","GERENTE", 1000000, 70000, 120000, 810000]];
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
funcion.imprimir_sueldos(lista,cargo);
