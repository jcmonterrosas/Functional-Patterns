from abc import ABC, abstractmethod

class ITipoConduccion(ABC):
    @abstractmethod
    def ObtenerDescripcion(self):
        pass
    def ObtenerPotencia(self, decilitrosCombustible):
        pass
    def ObtenerIncrementoVelocidad(self, decilitrosCombustible):
        pass

class Context():

    def __init__(self, TipoConduccion: ITipoConduccion) -> None:
        self._TipoConduccion = TipoConduccion

    @property
    def TipoConduccion(self) -> ITipoConduccion:
        return TipoConduccion._TipoConduccion

    @TipoConduccion.setter
    def TipoConduccion(self, TipoConduccion: ITipoConduccion) -> None:
        self._TipoConduccion = TipoConduccion

class ConduccionUrbana(ITipoConduccion):
    def ObtenerDescripcion(self):
        return "Conduccion Urbana"
    def ObtenerPotencia(self,decilitrosCombustible):
        return decilitrosCombustible * 0.842 + 3
    def ObtenerIncrementoVelocidad(self,decilitrosCombustible):
        return decilitrosCombustible * 0.422 + 2

class ConduccionDeportiva(ITipoConduccion):
    def ObtenerDescripcion(self):
        return "Conduccion Deportiva"
    def ObtenerPotencia(self,decilitrosCombustible):
        return decilitrosCombustible * 0.987 + 5
    def ObtenerIncrementoVelocidad(self,decilitrosCombustible):
        return decilitrosCombustible * 0.618 + 3

class ConduccionEjecutiva(ITipoConduccion):
    def ObtenerDescripcion(self):
        return "Conduccion Ejecutiva"
    def ObtenerPotencia(self,decilitrosCombustible):
        return decilitrosCombustible * 0.987 + 2
    def ObtenerIncrementoVelocidad(self,decilitrosCombustible):
        return decilitrosCombustible * 0.618 + 1

class Vehiculo:

  context=Context(ConduccionDeportiva())
 
  def ConduccionUrbana(self):
          self.context.TipoConduccion = ConduccionUrbana()
  
  def ConduccionEjecutiva(self):
          self.context.TipoConduccion = ConduccionEjecutiva()

  def ConduccionDeportiva(self):
          self.context.TipoConduccion=ConduccionDeportiva()

  def Acelerar(self,decilitrosCombustible):
          print("Tipo de conduccion: ",self.context._TipoConduccion.ObtenerDescripcion())
          print("Potencia añadida: ",self.context._TipoConduccion.ObtenerPotencia(decilitrosCombustible))
          print("Incremento de velocidad: ",self.context._TipoConduccion.ObtenerIncrementoVelocidad(decilitrosCombustible))

if __name__ == "__main__":
    Vehiculo = Vehiculo()
    Vehiculo.ConduccionDeportiva()
    Vehiculo.Acelerar(2.4)
    print()
    Vehiculo.ConduccionUrbana()
    Vehiculo.Acelerar(2.4)
    print()
    Vehiculo.ConduccionEjecutiva()
    Vehiculo.Acelerar(2.4)