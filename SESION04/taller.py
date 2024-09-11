"""Andres Felipe Tapias Barbosa"""


class CuentaBancaria:
    def __init__(self, numero_cta, nombre_cliente, saldo_cta, fecha_apertura):
        self.numero_cta = numero_cta
        self.nombre_cliente = nombre_cliente
        self.saldo_cta = saldo_cta
        self.fecha_apertura = fecha_apertura
        self.ultimo_retiro = 0
        self.ultima_consignacion = 0

    def consignar(self, monto):
        self.saldo_cta += monto
        self.ultima_consignacion = monto
        print("Consignación realizada correctamente.")

    def retirar(self, monto):
        if monto <= self.saldo_cta:
            self.saldo_cta -= monto
            self.ultimo_retiro = monto
            print("Retiro realizado correctamente.")
        else:
            print("Saldo insuficiente para realizar el retiro.")

    def mostrar_datos_cuenta(self):
        print(f"Número de cuenta: {self.numero_cta}")
        print(f"Titular: {self.nombre_cliente}")
        print(f"Saldo actual: {self.saldo_cta}")
        print(f"Fecha de apertura: {self.fecha_apertura}")
        print(f"Último retiro: {self.ultimo_retiro}")
        print(f"Última consignación: {self.ultima_consignacion}")


class CuentaDeAhorro(CuentaBancaria):
    def __init__(self, numero_cta, nombre_cliente, saldo_cta, fecha_apertura, tasa_interes, finalidad, liquidez):
        super().__init__(numero_cta, nombre_cliente, saldo_cta, fecha_apertura)
        self.tasa_interes = tasa_interes
        self.finalidad = finalidad
        self.liquidez = liquidez

    def calcular_interes(self):
        interes_generado = self.saldo_cta * (self.tasa_interes / 100)
        print(f"Interés generado: ${interes_generado:.2f}")


class CuentaCorriente(CuentaBancaria):
    def __init__(self, numero_cta, nombre_cliente, saldo_cta, fecha_apertura, linea_credito, pago_recu, aseso_ime):
        super().__init__(numero_cta, nombre_cliente, saldo_cta, fecha_apertura)
        self.linea_credito = linea_credito
        self.pago_recu = pago_recu
        self.aseso_ime = aseso_ime

    def emitir_cheque(self, monto):
        if monto <= self.saldo_cta + self.linea_credito:
            self.saldo_cta -= monto
            float (print(f"Se emitió un cheque por ${monto}."))
        else:
            print("Fondos insuficientes, incluso con la línea de crédito.")


def main():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Crear nueva cuenta de ahorros")
        print("2. Crear nueva cuenta corriente")
        print("3. Salir")
        opcion_principal = int(input("Ingrese una opcion: "))
        
        if opcion_principal == 1:
            numero_cta = int(input("Ingrese el número de cuenta: "))
            nombre_cliente = input("Ingrese el nombre del titular: ")
            saldo_inicial = float(input("Ingrese el saldo inicial: "))
            fecha_apertura = input("Ingrese la fecha de apertura: ")
            tasa_interes = float(input("Ingrese la tasa de interés: "))
            finalidad = input("Ingrese la finalidad de la cuenta de ahorros: ")
            liquidez = input("Ingrese la liquidez de la cuenta de ahorros: ")

            cuenta_ahorro = CuentaDeAhorro(numero_cta, nombre_cliente, saldo_inicial, fecha_apertura, tasa_interes, finalidad, liquidez)

            while True:
                print("\n--- Menú de opciones ---")
                print("1. Consultar saldo")
                print("2. Realizar consignación")
                print("3. Realizar retiro")
                print("4. Calcular interés")
                print("5. Mostrar datos de la cuenta")
                print("6. Volver al menú principal")
                opcion = int(input("Ingrese la opción deseada: "))

                if opcion == 1:
                    print(f"Saldo actual: {cuenta_ahorro.saldo_cta}")
                elif opcion == 2:
                    monto_consignacion = float(input("Ingrese el monto a consignar: "))
                    cuenta_ahorro.consignar(monto_consignacion)
                elif opcion == 3:
                    monto_retiro = float(input("Ingrese el monto a retirar: "))
                    cuenta_ahorro.retirar(monto_retiro)
                elif opcion == 4:
                    cuenta_ahorro.calcular_interes()
                elif opcion == 5:
                    cuenta_ahorro.mostrar_datos_cuenta()
                elif opcion == 6:
                    break
                else:
                    print("Opción no válida. Intente de nuevo.")

        elif opcion_principal == 2:
            numero_cta = int(input("Ingrese el número de cuenta: "))
            nombre_cliente = input("Ingrese el nombre del titular: ")
            saldo_inicial = float(input("Ingrese el saldo inicial: "))
            fecha_apertura = input("Ingrese la fecha de apertura: ")
            linea_credito = (input("Ingrese su línea de crédito: "))
            pago_recu = float(input("Ingrese su cuota de manejo: "))
            aseso_ime = "Usted tendrá acceso inmediato a todo su dinero"

            cuenta_corriente = CuentaCorriente(numero_cta, nombre_cliente, saldo_inicial, fecha_apertura, linea_credito, pago_recu, aseso_ime)

            while True:
                print("\n--- Menú de opciones ---")
                print("1. Consultar saldo")
                print("2. Realizar consignación")
                print("3. Realizar retiro")
                print("4. Emitir cheque")
                print("5. Mostrar datos de la cuenta")
                print("6. Volver al menú principal")
                opcion = int(input("Ingrese la opción deseada: "))

                if opcion == 1:
                    print(f"Saldo actual: {cuenta_corriente.saldo_cta}")
                elif opcion == 2:
                    monto_consignacion = float(input("Ingrese el monto a consignar: "))
                    cuenta_corriente.consignar(monto_consignacion)
                elif opcion == 3:
                    monto_retiro = float(input("Ingrese el monto a retirar: "))
                    cuenta_corriente.retirar(monto_retiro)
                elif opcion == 4:
                    monto_cheque = float(input("Ingrese el monto del cheque a emitir: "))
                    cuenta_corriente.emitir_cheque(monto_cheque)
                elif opcion == 5:
                    cuenta_corriente.mostrar_datos_cuenta()
                elif opcion == 6:
                    break
                else:
                    print("Opción no válida. Intente de nuevo.")
        
        elif opcion_principal == 3:
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
