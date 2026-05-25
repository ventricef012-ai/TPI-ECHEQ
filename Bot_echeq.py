import csv
import os

def guardar_factura(nro_factura, proveedor, monto, estado):
    archivo = "facturas.csv"
    with open(archivo, "a", newline="") as f:
        escritor = csv.writer(f)
        escritor.writerow([nro_factura, proveedor, monto, estado])
    print(f"Factura {nro_factura} registrada en el sistema.\n")

def actualizar_estado(estado_nuevo):
    archivo = "facturas.csv"
    filas = []
    with open(archivo, "r") as f:
        lector = csv.reader(f)
        for fila in lector:
            if fila[3] == "PENDIENTE":
                fila[3] = estado_nuevo
            filas.append(fila)
    with open(archivo, "w", newline="") as f:
        escritor = csv.writer(f)
        escritor.writerows(filas)
    print(f"Facturas actualizadas a estado {estado_nuevo}.\n")

def main():
    print("=" * 50)
    print("SISTEMA DE PAGO CON CHEQUES ELECTRONICOS (ECHEQ)")
    print("=" * 50)
    print()

    # Identificacion del usuario
    nombre = input("Ingrese su nombre: ")
    print(f"\nBienvenido, {nombre}.")
    print("Iniciando proceso de pago con Echeq...\n")

    # FASE 1 y 2 - Carga de facturas (pueden ser varias)
    while True:
        print("--- FASE 1: INGRESO DE FACTURA ---")
        nro_factura = input("Ingrese el número de factura: ")
        proveedor = input("Ingrese el nombre del proveedor: ")
        monto = input("Ingrese el monto de la factura: ")
        print(f"\nFactura {nro_factura} de {proveedor} por ${monto} recibida.")
        print("Revisando factura...\n")

        # FASE 2 - Compuerta 1: ¿Factura OK?
        print("--- FASE 2: AUTORIZACION ---")
        while True:
            factura_ok = input("¿La factura está OK? (si/no): ").strip().lower()
            if factura_ok == "si":
                print("Factura cargada en sistema correctamente.\n")
                guardar_factura(nro_factura, proveedor, monto, "PENDIENTE")
                break
            elif factura_ok == "no":
                print("Resolviendo con el proveedor...")
                print("Reingresando factura para revisión.\n")
            else:
                print("Respuesta inválida. Ingrese 'si' o 'no'.")

        # Preguntar si hay mas facturas
        while True:
            otra = input("¿Hay más facturas para cargar? (si/no): ").strip().lower()
            if otra == "si":
                break
            elif otra == "no":
                print("\nCarga de facturas finalizada. Continuando con Tesorería...\n")
                break
            else:
                print("Respuesta inválida. Ingrese 'si' o 'no'.")
        
        if otra == "no":
            break

    # FASE 3 - Tesoreria (se ejecuta una vez con todas las facturas cargadas)
    print("--- FASE 3: TESORERIA ---")
    print("Recibiendo facturas autorizadas (proceso semanal)...")

    while True:
        autorizadas = input("¿Las facturas están autorizadas? (si/no): ").strip().lower()
        if autorizadas == "si":
            print("Facturas autorizadas. Continuando proceso...\n")
            break
        elif autorizadas == "no":
            print("Facturas no autorizadas. Devolviendo a Compras para revisión.\n")
        else:
            print("Respuesta inválida. Ingrese 'si' o 'no'.")

    print("Emitiendo OPs y armando legajo...")
    print("Generando Excel echeq automáticamente...")
    while True:
        subir = input("¿El archivo fue subido al banco? (si/no): ").strip().lower()
        if subir == "si":
            print("Archivo subido correctamente.\n")
            break
        elif subir == "no":
            print("Por favor suba el archivo al banco para continuar.")
        else:
            print("Respuesta inválida. Ingrese 'si' o 'no'.")

    # FASE 4 - Firma y Emision
    print("--- FASE 4: FIRMA Y EMISION ---")
    while True:
        aprueba = input("¿El firmante aprueba el legajo y archivo? (si/no): ").strip().lower()
        if aprueba == "si":
            print("Legajo aprobado. Firmando en banco y emitiendo echeqs...\n")
            actualizar_estado("PAGADO")
            break
        elif aprueba == "no":
            print("Legajo rechazado. Corrigiendo y resubiendo archivo...")
            print("Archivo corregido. Volviendo a revisión del firmante.\n")
        else:
            print("Respuesta inválida. Ingrese 'si' o 'no'.")

    # Tareas automaticas finales
    print("Enviando comprobantes de pago al proveedor automáticamente...")
    print("Comprobantes enviados correctamente.")
    
    print("=" * 50)
    print("PROCESO FINALIZADO CORRECTAMENTE.")
    print("=" * 50)

main()