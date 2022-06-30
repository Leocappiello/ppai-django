from Controller.GestorRegistrarReservaTurnoRT import GestorRegistrarReservaTurnoRT

class PantallaRegistrarReservaTurnoRT:
    def __init__ (self, numeroRT, fechaAlta, imagenes, periodicidadMantenimientoPrev, duracionMatenimientoPrev, fraccionHorarioTurnos, ):
        self.__numeroRT = numeroRT
        self.__fechaAlta = fechaAlta
        self.__imagenes = imagenes
        self.__periodicidadMantenimientoPrev = periodicidadMantenimientoPrev
        self.__duracionMatenimientoPrev = duracionMatenimientoPrev
        self.__fraccionHorarioTurnos = fraccionHorarioTurnos
    
    def mostrarRT(self):
        return self.__numeroRT

    def habilitar(self):
        return

    def conocerCategoria(self):
        return

    def conocerCaracteristicaRecurso(self):
        return        

    def opcionReservarTurnoRT(self):
        self.habilitarVentana()

    def habilitarVentana(self):
        gestor = GestorRegistrarReservaTurnoRT()
        gestor.tomarOpcionReservarTurnoRT()

    def mostrarTipoRTParaSeleccion(self):
        #
        gestor = GestorRegistrarReservaTurnoRT()
        gestor