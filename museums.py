from datetime import datetime

VALID_TAGS = ["religion", "history", "art", "science"]

DAY_NUMBER_TO_STRING = {
    1:"Lunes",
    2:"Martes",
    3:"Miércoles",
    4:"Jueves",
    5:"Viernes",
    6:"Sábado",
    7:"Domingo"
}

class Museum():
    def __init__(
        self, 
        name, 
        opening_time, 
        closing_time, 
        entrance_price, 
        open_days=(2,3,4,5,6,7), 
        tags=[], 
        notes="", 
        requires_appointment=False,
        address=None):
        
            self.name = name
            self.opening_time = datetime.strptime(opening_time, "%H:%M")
            self.closing_time = datetime.strptime(closing_time, "%H:%M")
            self.open_days = open_days
            self.entrance_price = entrance_price
            self.tags = tags
            self.notes = notes
            self.requires_appointment = requires_appointment
            self.address = address
            self.id = None

    def print_data(self):
        print("Nombre:", self.name)
        print("ID:", self.id)
        print("Días: ", end="")
        for d in self.open_days:
            print(DAY_NUMBER_TO_STRING[d], ", ", end="", sep="")
        print("\nHorarios:", datetime.strftime(self.opening_time, "%H:%M"), "-", datetime.strftime(self.closing_time, "%H:%M"))
        print("Precio de entrada: ", (self.entrance_price if self.entrance_price is not None else "?"))
        if self.tags is None:
            print("Etiquetas: Ninguna")
        else:
            print("Etiquetas: ", end="")
            for t in self.tags:
                print(t, ", ", sep="", end="")
            print("\n", end="")
        print("Requiere pedir turno: ", ("Sí" if self.requires_appointment else "No"))
        if self.notes != "":
            print("Notas:", self.notes)
        

museums = [
    Museum("Museo Güemes", "11:00", "19:00", 0, address= "España 730, Salta, Salta, Argentina", tags=["history",]),
    Museum("MAAM", "11:00", "19:00", 600, address="Bartolomé Mitre 77, Salta, Salta, Argentina", notes="Gratis para salteños menores a 18 por enero y febrero", tags=["history",]),
    Museum("Museo de Antropologia de Salta", "9:00", "19:00", 0, address="Ejército del Norte y Ricardo Solá, Salta, Salta, Argentina", tags=["history", "science"], notes="Precio desconocido", ),
    Museum("Museo de Arte Contemporáneo", "9:00", "19:00", 0, address="Zuviría 90, Salta, Salta, Argentina", tags=["art",]),
    Museum("Museo de Bellas Artes de Salta", "9:00", "19:00", 0, address="Av. Belgrano 992, Salta, Salta, Argentina", tags=["art",], notes="Bono contribución"),
    Museum("Museo Casa de Arias Rengel", "10:00", "16:00", None, address="Peatonal La Florida 20, Salta, Salta, Argentina", tags=["art", "history"], requires_appointment=True),
    Museum("Museo Histórico del Norte", "14:00", "17:00", 0, address="Caseros 549, Salta, Salta, Argentina", tags=["history",], notes="los sábados abre hasta las 17:30"),
    Museum('Museo de la Ciudad "Casa de Hernandez"', "10:00", "19:00", 0, address="Peatonal La Florida 97, Salta, Salta, Argentina", tags=["history",]),
    Museum("Museo de la Basílica San Francisco", "16:00", "19:00", 700, address="Córdoba 33, Salta, Salta, Argentina", tags=["religion",], requires_appointment=True),
    Museum("Museo Catedralicio Monseñor Carlos Mariano Perez", "17:00", "20:00", 0, (1, 2, 3, 4 , 5, 6, 7), address="España 558, Salta, Salta, Argentina", tags=["religion",]),
    Museum("Museo Casa de Uriburu", "9:00", "17:00", 0, address="Caseros 417, Salta, Salta, Argentina", tags=["history",], notes="Sábados de 14:00 a 17:30 Hs. Domingos de 10:00 a 14:00 Hs."),
    Museum('Museo de Ciencias Naturales “Lic. Miguel A. Arra”', "15:00", "19:00", 200, address="Mendoza 2, Salta, Salta, Argentina", tags=["science",]),
    Museum('Museo Histórico de la Universidad Nacional de Salta, "Prof. Eduardo Ashur"', "15:00", "18:00", None, (2, 3, 4, 5), address="Buenos Aires 177, Salta, Salta, Argentina", tags=["history",])   
] 

museum_id_list = []
for i, m in enumerate(museums):
    m.id = i
    museum_id_list.append(i)