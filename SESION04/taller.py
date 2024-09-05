class CuentaBancaria:
    def _init_(self, numeroCta="", nombreCliente="", saldoCta=0.0, fechaApertura=None):
        if fechaApertura is None:
            fechaApertura = datetime.now()
        self.__numeroCta = numeroCta
        self.__nombreCliente = nombreCliente
        self.__saldoCta = saldoCta
        self.__fechaApertura = fechaApertura
        self.__ultimoRetiro = None
        self.__ultimaConsignacion = None

    def set(self, numeroCta, nombreCliente, saldoCta, fechaApertura=None):
        self.__numeroCta = numeroCta
        self.__nombreCliente = nombreCliente
        self.__saldoCta = saldoCta
        if fechaApertura is None:
            self.__fechaApertura = datetime.now()
        else:
            self.__fechaApertura = fechaApertura

    def set_numeroCta(self, numeroCta):
        self.__numeroCta = numeroCta

    def set_nombreCliente(self, nombreCliente):
        self.__nombreCliente = nombreCliente

    def set_saldoCta(self, saldoCta):
        if saldoCta < 0:
            self.__saldoCta = 0
        else:
             self.__saldoCta = saldoCta

    def set_fechaApertura(self, fechaApertura):
        self.__fechaApertura = fechaApertura

    def get_numeroCta(self):
        return self.__numeroCta

    def get_nombreCliente(self):
        return self.__nombreCliente

    def get_saldoCta(self):
        return self.__saldoCta

    def get_fechaApertura(self):
        return self.__fechaApertura

    def get_ultimoRetiro(self):
        return self.__ultimoRetiro

    def get_ultimaConsignacion(self):
        return self.__ultimaConsignacion

    def consignar(self, monto):
        if monto > 0:
            self.__saldoCta += monto
            self.__ultimaConsignacion = datetime.now()
            print(f"Consignación exitosa. Nuevo saldo: {self.__saldoCta}")
        else:
             print("El monto debe ser mayor a cero.")

    def retirar(self, monto):
        if monto > 0:
            if self.__saldoCta >= monto:
                self.__saldoCta -= monto
                self.__ultimoRetiro = datetime.now()
                print(f"Retiro exitoso. Nuevo saldo: {self.__saldoCta}")
        else:
                print("Saldo insuficiente.")
        else:
            print("El monto debe ser mayor a cero.")

    def transferencia(self, monto, cuenta_destino):
        if monto > 0:
            if self.__saldoCta >= monto:
                self.retirar(monto)
                cuenta_destino.consignar(monto)
                print(f"Transferencia exitosa a la cuenta {cuenta_destino.get_numeroCta()}.")
            else:
                print("Saldo insuficiente para la transferencia.")
        else:
            print("El monto debe ser mayor a cero.")
