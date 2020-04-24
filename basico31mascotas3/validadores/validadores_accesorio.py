
import re
expresion_mascota = "^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]{2,60}$"
expresion_accesorio = "^[0-9]{1,5}$"


def validar_mascota(mascota):
    validador = re.compile(expresion_mascota)
    return validador.match(mascota)

def validar_accesorio(accesorio):
    validador = re.compile(expresion_accesorio)
    return validador.match(accesorio)