"""
Proyecto - Introducción a la Programación
Avance 2
Caso: Desarrollo de Software de Fraude para banco MyOwnMoney

Descripción del caso: El Banco MyOwnMoney requiere un sistema para que sus empleados
registren y analicen fraudes digitales (TEF, e-commerce, TerryPay) en cuentas corrientes.
El objetivo es centralizar los reclamos de los clientes, investigar los movimientos objetados
y generar informes técnicos de respuesta.

Funcionalidad del Software
Consultas: Permite visualizar la lista de clientes del banco, detalles de transferencias (ID, banco, monto)
y el estado de los reclamos ("En investigación").

Métricas Globales: Muestra totales estáticos de dinero en fraude y saldos a nivel de todo el banco.

Métricas Individuales: Calcula de forma automática la suma de TEF, pagos y montos en reclamo para una cuenta
específica, además de proyectar un saldo disponible.

Semana 5

Grupo 3 
Integrentes:   
- Paula Arroyo Salvo 
- Nathalya Canales Álvarez 
- Karel Escudero Vinciguerra 
- Javiera Fuentealba Rojas 
- José Méndez Maringuer
- Carlos Muñoz Mondaca

"""

# VARIABLES DE CONTROL Y MENÚ 
opcion_menu = 0  # Opción seleccionada en el menú principal 
tipo_consulta = 0  # Tipo de consulta seleccionada
categoria = 0  # Categoría elegida para visualizar totales 
alcance = 0  # Define si el cálculo es individual o global 
continuar = True  # Indica si el sistema continúa ejecutándose 

# VARIABLES DE CLIENTE
rut_cliente = "18754901-3"  # Identifica de forma única al cliente 
nombre = "Juanita Perez"  # Nombre completo del cliente 
numero_cuenta = "89827183"  # Número de cuenta corriente del cliente 
saldo = 500000  # Saldo disponible en la cuenta del cliente 

# VARIABLES DE TRANSFERENCIA (TEF) 
id_tef = 93494  # Identificador único de la transferencia 
fecha = "13-02-25"  # Fecha en que se realiza la transacción 
hora = "12:00:00"  # Hora en que se realiza la transacción 
monto = 100000  # Monto de la operación (TEF o pago) 
banco_destino = "Banco YouOwnMoney"  # Banco al que se transfiere el dinero 
rut_destinatario = "12345678-9"  # RUT de la persona que recibe el dinero 
cuenta_destino = "927463"  # Cuenta bancaria destino de la transferencia 
comentario = "Trasferencia Agua"  # Descripción de la transacción 

# VARIABLES DE PAGO
id_pago = 384735  # Identificador único del pago 
rut_comercio = "77984242-3"  # RUT del comercio donde se realiza el pago 
fecha = "13-04-25" #Fecha Pago
hora = "12:00:00" #Hora Pago
monto = 150000 #Monto del Pago


# VARIABLES DE RECLAMO
id_reclamo = 0  # Identificador único del reclamo 
descripcion = "Me di cuenta hoy, al ver menos dinero en mi cuenta corriente"  # Detalle del reclamo del cliente 
monto_reclamado = 500000  # Monto total reclamado por fraude 
estado = "En proceso"  # Estado del reclamo (en proceso, validado, cerrado) 
numero_cuenta = "89827183"  # Relaciona el reclamo con el cliente 

# VARIABLES DE TOTALES (MÉTRICAS GLOBALES) 
total_saldo = 1500000000  # Suma total del dinero de todos los clientes 
total_tef = 125000000  # Suma total de transferencias TEF 
total_pagos = 4548005400  # Suma total de pagos realizados 
total_reclamos = 47639  # Suma total de dinero reclamado




while True:
    print("\n============================================================")
    print("           BANCO MYOWNMONEY - REGISTRO DE FRAUDES           ")
    print("============================================================")
    print("1. Lista Clientes registrados")
    print("2. Visualización Global (Métricas del Banco)")
    print("3. Consulta Detallada por número de cuenta")
    print("4. Finalizar Sesión")
    print("------------------------------------------------------------")

    opcion_menu = int(input("Seleccione opción del 1 al 4: "))
    

    if opcion_menu == 1:
        print("\n>> LISTADO: RUT | NOMBRE | CUENTA")
        print(f"{rut_cliente} | {nombre} | {numero_cuenta}")
        print("11.222.333-4 | Pedrito Rios | 445566")

    elif opcion_menu == 2:
        print("\n--- CONSULTA DE MÉTRICAS GLOBALES ---")
        print("1. Total Saldo Clientes")
        print("2. Total en Transferencias (TEF)")
        print("3. Total en Pagos")
        print("4. Total en Reclamos")
        print("5. Ver Resumen Completo")
        print("-------------------------------------")
        
        categoria = int(input("Seleccione el total que desea visualizar: "))

        if categoria == 1:
            print(f"\n>> TOTAL SALDO BANCO: ${total_saldo}")
        elif categoria == 2:
            print(f"\n>> TOTAL MONTO TEF: ${total_tef}")
        elif categoria == 3:
            print(f"\n>> TOTAL MONTO PAGOS: ${total_pagos}")
        elif categoria == 4:
            print(f"\n>> TOTAL MONTO RECLAMOS: ${total_reclamos}")
        elif categoria == 5:
            print("\n>> RESUMEN GLOBAL DEL BANCO")
            print(f"Saldo Total: ${total_saldo}")
            print(f"Total TEF:   ${total_tef}")
            print(f"Total Pagos: ${total_pagos}")
            print(f"Reclamos:    ${total_reclamos}")
        else:
            print("Opción de categoría no válida.")

    elif opcion_menu == 3:
        numero_cuenta = input("\nIngrese numero_cuenta: ")
        print(f"\n>> DETALLE PARA CUENTA: {numero_cuenta}")
        print("1. Ver TEF | 2. Ver Pagos | 3. Ver Reclamos")
        
        tipo_consulta = int(input("Seleccione tipo de consulta: "))
        
        if tipo_consulta == 1:
            print("\n>> DETALLE DE TRANSACCIONES TEF (Individual)")
            print(f"ID: {id_tef} | DESTINO: {banco_destino} | MONTO: $250000")
            print("FECHA: 24/03/2015 | RUT DEST: 18.458.743-2")
        
        elif tipo_consulta == 2:
            print("\n>> DETALLE DE PAGOS")
            print("ID: 440 | COMERCIO: 76.123.456-K | MONTO: $80000")
            print("FECHA: 24/03/2015 | HORA: 12:00:00")

        elif tipo_consulta == 3:
            print("\n>> INFORME DETALLADO DE RECLAMOS")
            print("ID RECLAMO: 001 | ESTADO: En investigacion")
            print("DESCRIPCION: Me di cuenta ayer cuando vi que tenia menos dinero")

    elif opcion_menu == 4:
        print("Cerrando sesión... Gracias por usar el sistema del Banco MyOwnMoney.")
        break

    else:
        print("Opción no válida. Intente nuevamente.")




