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
