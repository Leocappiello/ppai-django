from centivfacultad.classes.Model.RecursoTecnologico import RecursoTecnologico

class TipoRecursoTecnologico:
    def __init__ (self):
        return
    def getNombre(self, resource):
        return resource['name']
    def buscarDatosRTSeleccionado(self):
        recurso = RecursoTecnologico()
        recurso.getNumeroRT()