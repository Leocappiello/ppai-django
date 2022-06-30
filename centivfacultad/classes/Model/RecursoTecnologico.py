import json
import os.path
from TipoRecursoTecnologico import TipoRecursoTecnologico


class RecursoTecnologico:
    def __init__(self):
        return

    def buscarTipoRT(self):
        #print(os.path.join(os.path.dirname(__file__), '/../data/resourcesCopy.json'))
        f = os.path.join(os.path.dirname(
            __file__), '/Users/Leo/Documents/des/django-ppai/centivfacultad/data/resourcesCopy.json')
        data = open(f, encoding='utf-8')
        data = json.load(data)
        # print(data[0]['name'])
        #print(len(data))
        
        for resource in data:
            tipoRecurso = TipoRecursoTecnologico()
            tipoRecurso.getNombre(resource)
        #print(tipoRecurso.getNombre(resource))

    def getNumeroRT(self):
        return
            

#recurso = RecursoTecnologico()
#recurso.buscarTipoRT()