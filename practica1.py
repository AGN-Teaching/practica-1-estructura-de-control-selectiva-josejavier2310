# Introduccion
print("Programacion estructurada")
print("Nombre: Jose Javier Perez Ledesma")
print("Practica 1: Estructura de control selectiva")
def calcular_sueldo_neto():
    # Datos de entrada
    salario_por_hora = float(input("Salario por hora: "))
    horas_trabajadas = float(input("Horas trabajadas en el mes: "))
    # Cálculo del sueldo bruto
    if horas_trabajadas <= 160:
        sueldo_bruto = salario_por_hora * horas_trabajadas
    elif horas_trabajadas <= 200:
        sueldo_bruto = (160 * salario_por_hora) + ((horas_trabajadas - 160) * salario_por_hora * 1.5)
    else:
        sueldo_bruto = (160 * salario_por_hora) + (40 * salario_por_hora * 1.5) + ((horas_trabajadas - 200) * salario_por_hora * 2)
    # Tabla de ISR
    tabla_isr = [
        (0.01, 746.04, 0.00, 1.92), (746.05, 6332.05, 14.32, 6.40), 
        (6332.06, 11128.01, 371.83, 10.88), (11128.02, 12935.82, 893.63, 16.00),
        (12935.83, 15487.71, 1182.88, 17.92), (15487.72, 31236.49, 1640.18, 21.36),
        (31236.50, 49233.00, 5004.12, 23.52), (49233.01, 93993.90, 9236.89, 30.00),
        (93993.91, 125325.20, 22665.17, 32.00), (125325.21, 375975.61, 32691.18, 34.00),
        (375975.62, float('inf'), 117912.32, 35.00)
    ]
    # Cálculo del ISR
    for limite_inferior, limite_superior, cuota_fija, porcentaje in tabla_isr:
        if limite_inferior <= sueldo_bruto <= limite_superior:
            isr = cuota_fija + ((sueldo_bruto - limite_inferior) * (porcentaje / 100))
            break
    # Descuentos
    print("Opciones a eleguir")
    print("1. Cuota Fija")
    print("2. Cuota Porcentual")
    seleccion = input("Eligue una opcion")
    if seleccion == "1":
        caja_ahorro = caja_ahorro + 1000.00
    elif seleccion == "2":
        print("Cual de estos dos puntos")
        print("1. El 3% del sueldo bruto mensual")
        print("2. El 5% del sueldo bruto mensual")
        punto = input("Elige uno de esos puntos")
        if punto == "2":
            seguridad_social = sueldo_bruto * 0.025
        elif punto == "1":
            caja_ahorro = sueldo_bruto * 0.03
    
    #Pedimos al usuari que si quiere participar en el ahorro solidario
    print(" Otras Opciones para eleguir")
    print("1. No participar")
    print("2. 1% Sueldo bruto mensual")
    print("3. 2% del sueldo mensual")
    opcion = input("Elie una opcion")
    if opcion == "2":
        ahorro_solidario = sueldo_bruto * 0.01
    elif opcion == "3":
        ahorro_solidario = sueldo_bruto * 0.02
    else
        ahorro_solidario = 0.00
                   
    # Cálculo del sueldo neto
    sueldo_neto = sueldo_bruto - (isr + seguridad_social + caja_ahorro + ahorro_solidario)
    # Resultados
    print("\n--- Resumen ---")
    print(f"Sueldo Bruto: ${sueldo_bruto:.2f}")
    print(f"ISR: ${isr:.2f}")
    print(f"Seguridad Social: ${seguridad_social:.2f}")
    print(f"Caja de Ahorro (3%): ${caja_ahorro:.2f}")
    print(f"Ahorro Solidario (1%): ${ahorro_solidario:.2f}")
    print(f"Sueldo Neto: ${sueldo_neto:.2f}")
# Ejecutar el cálculo
calcular_sueldo_neto() 
