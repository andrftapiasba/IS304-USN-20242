class CuentaBancaria:  
  
  def _init_(self,numeroCta,nombreCliente, saldoCta,fechaApertura,ultimoRetiro,ultimaConsignacion):
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
