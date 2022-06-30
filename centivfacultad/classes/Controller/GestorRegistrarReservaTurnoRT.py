from Model.RecursoTecnologico import RecursoTecnologico
from Model.Estado import Estado
from Model.CentroInvestigacion import CentroInvestigacion

class GestorRegistrarReservaTurnoRT:
    def __init__(self):
        return

    def tomarOpcionReservarTurnoRT(self):
        self.buscarTipoRT()

    def buscarTipoRT(self):
        resource = RecursoTecnologico()
        resource.buscarTipoRT()
    
    def tomarSeleccionTipoRT(self):
        return self.buscarEstadoDisponible()
    
    def buscarEstadoDisponible(self):
        estado = Estado()
        estado.esAmbitoRT()
        estado.esDisponible()
    
    def buscarCI(self):
        #
        centro = CentroInvestigacion()
        centro.getNombre()
    
    def buscarDatosRTSeleccionadoSegunCI(self):
        return