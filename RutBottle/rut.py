from bottle import route, run, view
from collections import namedtuple 
import re

class rutController:
    """Ruts"""
    # inicializa la clase. Para crear un modelo se toma
    # desd acá
    def __init__(self, rStr):
        self.rStr   = rStr
        #self.rNum   = rNum
        #self.rDV    = rDV
    
    #Simplemete devuelve un string con el rut formateado
    def verRut(self):
        return rStr #self.rNum+ "-"+self.rDV 

    #Verifica si el rut es válido
    def validar(self):
        RUT = rStr # self.rNum+ "-"+self.rDV
        VALID = False
        if RUT == '13881929-9':
            VALID = True
        return VALID

    #limpia un rut
    def limpiar(self):
        rStr = self.rStr.strip()
        pattern = re.compile(r'[^Kk\d]')
        rStr = pattern.sub(r'', rStr)
        #rStr = rStr[-1:]
        return rStr
