class CuentaBancaria:  
  
  def init(self,numeroCta,nombreCliente, saldoCta,fechaApertura,ultimoRetiro,ultimaConsignacion):
    self.__numeroCta= numeroCta
    self.__nombreCliente=nombreCliente
    self.__saldoCta= saldoCta
    self.__fechaApertura=fechaApertura
    self.__ultimoRetiro=ultimoRetiro
    self.__ultimaConsignacion=ultimaConsignacion
    
  def set(self,numeroCta,nombreCliente,saldoCta,fechaApertura,ultimoRetiro,ultimaConsignacion):
    self.__numeroCta=numeroCta
    self.__nombreCliente=nombreCliente
    self.__saldoCta= saldoCta
    self.__fechaApertura=fechaApertura
    self.__ultimoRetiro=ultimoRetiro
    self.__ultimaConsignacion=ultimaConsignacion
    
  def set_numeroCta(self, x):
        self.__numeroCta = x

  def set_nombreCliente(self, x):
        self.__nombreCliente=x
        
  def set_saldoCta(self, x):
        self.__saldoCta=x     
        
  def set_fechaApertura(self, x):
        self.__fechaApertura=x     
        
  def set_ultimoRetiro(self, x):
        self.__ultimoRetiro=x    
        
  def set_ultimaConsignacion(self, x):
        self.__ultimaConsignacion=x             


  def get_numeroCta(self):
        return self.__numeroCta
        
  def get_nombreCliente(self):
        return self.__nombreCliente
        
  def get_saldoCta(self,monto):
        return self.__saldoCta  
        
  def get_fechaApertura(self):
        return self.__fechaApertura
        
  def get_ultimoRetiro(self,fecha):
        return self.__ultimoRetiro
        
  def get_ultimaConsignacion(self, fecha):
        return self.__ultimaConsignacion
        
        
        
  def consignar(self, monto):
        if monto > 0:
            self.__saldo_cta += monto
            self.__ultima_consignacion = datetime.now()
            return True
        return False

  def retirar(self, monto):
        if monto > 0 and monto <= self.__saldo_cta:
            self.__saldo_cta -= monto
            self.__ultimo_retiro = datetime.now()
            return True
        return False
        
  def transferir(self, otra_cuenta, monto):
        if self.retirar(monto):
            otra_cuenta.consignar(monto)
            return True
        return False
        
  def menu():
    cuentas = {}
      
    while True:
        print("\n--- Menú Principal ---")
        print("1. Apertura de Cuenta")
        print("2. Consignar")
        print("3. Retirar")
        print("4. Transferir")
        print("5. Mostrar Información de Cuenta")
        print("6. Salir")
        
        
opcion=input ("Seleccione una opción: ")    
