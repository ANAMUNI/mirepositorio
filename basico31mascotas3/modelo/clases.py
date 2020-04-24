class Accesorio():
    
    def __init__(self, mascota = "", accesorio = "", talla = "", tipo = "", precio = 0.0,\
                  ofertas = False, cliente = "si", envio = "standar", id = 0):
        self.mascota = mascota
        self.accesorio = accesorio
        self.talla = talla
        self.tipo = tipo
        self.precio  = precio
        self.ofertas = ofertas
        self.cliente = cliente
        self.envio = envio
        self.id = id