# Lista de dias de la semana
diaSemanal = []
horasSemanal = []
mayor_y_menor = ["mayor horas laboradas", "Menor Horas laboradas"]


# subprograma de los datos del empleado
def calculosmatematicossinhorasextras(total_horas, valor_sin_horas_extras, salario_bruto_sin_horas_extra):
    if sum(horasSemanal) <= 40:
        total_horas = sum(horasSemanal)
        salario_bruto_sin_horas_extra = total_horas * valor_sin_horas_extras
    return total_horas, salario_bruto_sin_horas_extra


def calculomatematicoconhorasextra(total_horas,valor_sin_horas_extras,horas_extras,salario_bruto_con_horas_extra,salario_bruto_sin_horas_extra):
    total_horas=sum(horasSemanal)
    horas_extra = total_horas - 40
    salario_total_con_horas_extras=0
    if total_horas > 40:
        salario_bruto_sin_horas_extra = 40 * valor_sin_horas_extras
        horas_extra = total_horas - 40
        salario_bruto_con_horas_extra = horas_extras * 5000
        salario_total_con_horas_extras = salario_bruto_con_horas_extra + salario_bruto_sin_horas_extra
    return salario_bruto_sin_horas_extra,horas_extra,salario_total_con_horas_extras

def datosempleados(nombre, cedula):
    print("Bienvenido a nuestro programa", nombre, "que porta la cedula de identidad", cedula, end="")
    print("Este programa te ayuda a saber tu salario actual sin horas extras y con horas extras ")


def ingresarlosdatoslarales():
    i = 0
    while i != 6:
        dia = input("Digite el dia que laboro\n")
        diaSemanal.append(dia)
        horasLaborales = int(input("Digite la cantidad de hora que laboro en ese dia"))
        horasSemanal.append(horasLaborales)
        i += 1
    print("\t\t\tLos datos obtenidos por medio de nuestro programa\t\t\t ")
    x = 0
    y = 0
    print("\n      Dia        \t\t\t", "Horas laboradas")
    print()
    while x != 6:
        print("\n", diaSemanal[x], "\t\t\t", horasSemanal[y], "\t\t\t")

        x += 1
        y += 1
    total_horas = horasSemanal[0] + horasSemanal[1] + horasSemanal[2] + horasSemanal[3] + horasSemanal[4] + \
                  horasSemanal[5]
    print("Total de horas laboradas\t\t\t\t", total_horas)


def mayorymenorhoras():
    x = 0
    y = 0
    z = 0
    print("Mayor horas laboradas durante la semana")
    while y != 6:
        print("\n", diaSemanal[x], "\t\t\t", horasSemanal[y], "\t\t\t", mayor_y_menor[z])

        x += 1
        y += 1
        z += 1

       if horasSemanal[0]>horasSemanal[1]:

       if horasSemanal[1]>horasSemanal[2]:

       if horasSemanal[2] > horasSemanal[3]:

       if horasSemanal[3] > horasSemanal[4]:

       if horasSemanal[4]>horasSemanal[5]:





def calculodesalariobruto(valor_sin_horas_extras, valor_con_horas_extras, cedula, nombre, salario_bruto_sin_horas_extra,
                          salario_total):
    horas_extras = 0
    salario_bruto_sin_horas_extras = 0
    salario_bruto_con_horas_extra = 0
    total_horas = horasSemanal[0] + horasSemanal[1] + horasSemanal[2] + horasSemanal[3] + horasSemanal[4] + \
                  horasSemanal[5]

    if total_horas <= 40:
        salario_bruto_sin_horas_extra = total_horas * valor_sin_horas_extras
        print("Las horas sin horas extras que hizo el empleado fue de", total_horas,
              "El salario bruto sin horas extra es", salario_bruto_sin_horas_extra)
        print("El salario bruto total semanal es", salario_bruto_sin_horas_extra)
    if total_horas > 40:
        salario_bruto_sin_horas_extra = 40 * valor_sin_horas_extras
        horas_extra = total_horas - 40
        salario_bruto_con_horas_extra = horas_extras * 5000
        salario_total = salario_bruto_con_horas_extra + salario_bruto_sin_horas_extra
        print()
        print("\t\t\t salario bruto \t\t\t")
        print("nombre del funcionario", nombre)
        print("Cedula", cedula)
        print("Las horas sin horas extras que hizo el empleado fue de", 40, "El salario bruto sin horas extra es",
              salario_bruto_sin_horas_extra)
        print("El salario bruto total semanal es", salario_bruto_sin_horas_extra)
        print("Las horas extras que hizo el empleado fue de", horas_extra, "El salario bruto con horas extras es",
              end="")
        print(salario_bruto_con_horas_extra)
        print("Salario total sin horas extras y con horas extras es de", salario_total)


def calculodesalarioneto(cedula, nombre, salario_bruto_sin_horas_extra, total_horas):
    # valores sin horas extras
    horas_extras = 0
    valor_sin_horas_extras = 2500
    valor_con_horas_extras = 5000
    total_horas = sum(horasSemanal)
    salario_bruto_sin_horas_extra = total_horas * valor_sin_horas_extras
    horas_extra = total_horas - 40
    salario_bruto_con_horas_extra = horas_extras * 5000
    salario_total = salario_bruto_con_horas_extra + salario_bruto_sin_horas_extra
    deducción_ccss_sin_horas = salario_bruto_sin_horas_extra * 0.09
    deduccion_banco_popular_sin_horas = salario_bruto_sin_horas_extra * 0.01
    deducción_asociación_sin_horas = salario_bruto_sin_horas_extra * 0.05
    salario_neto = salario_bruto_sin_horas_extra - deducción_ccss_sin_horas - deduccion_banco_popular_sin_horas - deducción_asociación_sin_horas

    if total_horas <= 40:
        print("El nombre del funcionario es", nombre)
        print("Cedula", cedula)
        print("\t\t\tColilla de salario semanal sin horas extra\t\t\t")
        print("deducción de CCSS sin las horas extras", deducción_ccss_sin_horas)
        print("deducción de banco popular sin horas extras es", deduccion_banco_popular_sin_horas)
        print("deducción de asociacion solidarista es", deducción_asociación_sin_horas)
        print("Salario neto sin horas extras y ni deducciones", salario_bruto_sin_horas_extra)
        print("Salario neto sin horas extras", salario_neto)
    # Valores de salarios extras

    deducción_ccss_con_horas = salario_total * 0.09
    deduccion_banco_popular_con_horas = salario_total * 0.01
    deducción_asociación_con_horas = salario_total * 0.05
    salario_neto_con_horas = salario_total - deducción_ccss_con_horas - deduccion_banco_popular_con_horas - deducción_asociación_con_horas
    if total_horas > 40:
        print("El nombre del funcionario es", nombre)
        print("Cedula", cedula)
        print("\t\t\tColilla de salario semanal con horas extra\t\t\t")
        print("deducción de CCSS con las horas extras", deducción_ccss_con_horas)
        print("deducción de banco popular con horas extras es", deduccion_banco_popular_con_horas)
        print("deducción de asociacion solidarista es", deducción_asociación_con_horas)
        print("Salario neto con horas extras y ni deducciones", salario_bruto_sin_horas_extra)
        print("Salario neto con horas extras", salario_neto_con_horas)
        print("Gracias por visitar nuestro programa que tenga un buen dia")


def main():
    # creación de parametros
    salario_bruto_sin_horas_extra = 0
    horas_extras = 0
    valor_sin_horas_extras = 2500
    valor_con_horas_extras = 5000
    total_horas = sum(horasSemanal)
    salario_bruto_sin_horas_extra = total_horas * valor_sin_horas_extras
    horas_extra = total_horas - 40
    salario_bruto_con_horas_extra = horas_extras * 5000
    salario_total = salario_bruto_con_horas_extra + salario_bruto_sin_horas_extra
    print("\t\t\t Programa de calculo salarial los Melocotones S.A\t\t\t")
    print("Bienvenido al programa que te permite calcular tu salario bruto y neto semanalmente a todos nuestros")
    nombre = input("Digite el nombre completo del empleado")
    cedula = int(input("Digite el numero de cedula"))
    while True:
        print("Seleccione uno de los datos que aparece en nuestro menu")
        print("1- datos principal")
        print("2- Ingresar los datos laborales")
        print("3- Mayor y menor horas laborales")
        print("4- Calculo de salario bruto")
        print("5- calculo de dalario neto")
        print("6- Salir")
        print()
        y = int(input("Digite el numero del menu que desea ingresar"))

        if y == 1:
            print("Bienvenido a la pagina principal, en esta pagina tendras que llenar los datos solicitados")
            datosempleados(nombre, cedula)
            continue
        if y == 2:
            print("Esta pagina te permite llenar los datos laboradas en la empresa semanalmente")
            ingresarlosdatoslarales()
            print("fin de la sección de ingresar datos laborales")
            continue
        if y == 3:
            print("Esta pagina te permite saber cuales dias fue las horas mas laboradas y las menos laboradas ")
            mayorymenorhoras()
            print("fin de la sección de datos mayor y menor horas laboradas ")
            continue
        if y == 4:
            calculodesalariobruto(valor_sin_horas_extras, valor_con_horas_extras, cedula, nombre)
            continue

        if y == 5:
            calculodesalarioneto(cedula, nombre, salario_bruto_sin_horas_extra, total_horas)
            continue

        if y == 6:
            print("Gracias por visitarnos ")
            break

        else:
            print("Error, intente nuevamente en el programa")


main()
