from datetime import datetime

class CuentaBancaria:
    def __init__(self, numero_cta, nombre_cliente, saldo_cta, fecha_apertura):
        self.__numero_cta = numero_cta
        self.__nombre_cliente = nombre_cliente
        self.__saldo_cta = saldo_cta
        self.__fecha_apertura = fecha_apertura
        self.__ultimo_retiro = None
        self.__ultima_consignacion = None

    # Métodos getter y setter para numero_cta
    def get_numero_cta(self):
        return self.__numero_cta
    
    def set_numero_cta(self, numero_cta):
        self.__numero_cta = numero_cta

    # Métodos getter y setter para nombre_cliente
    def get_nombre_cliente(self):
        return self.__nombre_cliente
    
    def set_nombre_cliente(self, nombre_cliente):
        self.__nombre_cliente = nombre_cliente

    # Métodos getter y setter para saldo_cta
    def get_saldo_cta(self):
        return self.__saldo_cta
    
    def set_saldo_cta(self, saldo_cta):
        self.__saldo_cta = saldo_cta

    # Métodos getter y setter para fecha_apertura
    def get_fecha_apertura(self):
        return self.__fecha_apertura
    
    def set_fecha_apertura(self, fecha_apertura):
        self.__fecha_apertura = fecha_apertura

    # Métodos getter y setter para ultimo_retiro
    def get_ultimo_retiro(self):
        return self.__ultimo_retiro
    
    def set_ultimo_retiro(self, ultimo_retiro):
        self.__ultimo_retiro = ultimo_retiro

    # Métodos getter y setter para ultima_consignacion
    def get_ultima_consignacion(self):
        return self.__ultima_consignacion
    
    def set_ultima_consignacion(self, ultima_consignacion):
        self.__ultima_consignacion = ultima_consignacion

    def consignar(self, cantidad):
        if cantidad > 0:
            self.__saldo_cta += cantidad
            self.__ultima_consignacion = datetime.now()
            print(f"Se han consignado {cantidad} a la cuenta {self.__numero_cta}.")
        else:
            print("La cantidad a consignar debe ser positiva.")

    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.__saldo_cta:
                self.__saldo_cta -= cantidad
                self.__ultimo_retiro = datetime.now()
                print(f"Se han retirado {cantidad} de la cuenta {self.__numero_cta}.")
            else:
                print("Saldo insuficiente.")
        else:
            print("La cantidad a retirar debe ser positiva.")

    def transferir(self, cantidad, cuenta_destino):
        if cantidad > 0:
            if cantidad <= self.__saldo_cta:
                self.__saldo_cta -= cantidad
                self.__ultimo_retiro = datetime.now()
                cuenta_destino.consignar(cantidad)
                print(f"Se han transferido {cantidad} a la cuenta {cuenta_destino.get_numero_cta()}.")
            else:
                print("Saldo insuficiente.")
        else:
            print("La cantidad a transferir debe ser positiva.")

    def mostrar_info(self):
        print(f"Número de cuenta: {self.__numero_cta}")
        print(f"Nombre del cliente: {self.__nombre_cliente}")
        print(f"Saldo de la cuenta: {self.__saldo_cta}")
        print(f"Fecha de apertura: {self.__fecha_apertura.strftime('%d/%m/%Y')}")
        print(f"Último retiro: {self.__ultimo_retiro}")
        print(f"Última consignación: {self.__ultima_consignacion}")
