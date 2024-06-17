def imprimir_sueldos(lista,cargo):
    with open('Planilla_Sueldos.txt', 'w', encoding= "utf-8") as archivo:
        archivo.write("Trabajador - Cargo - Sueldo Bruto  - Desc. Salud Desc. - AFP Líquido a pagar\n");
        for i in lista:
            if cargo == "TODOS":
                archivo.write(f"{i[0]} - {i[1]} - {i[2]} - {i[3]} - {i[4]}\n");
            else:
                if cargo.upper() == i[1]:
                    archivo.write(f"{i[0]} - {i[1]} - {i[2]} - {i[3]} - {i[4]}\n");