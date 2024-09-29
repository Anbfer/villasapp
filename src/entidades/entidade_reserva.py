class Reserva:
    def __init__(self, id_morador, id_reserva, data_reserva, area_reserva):
        self.__id_reserva = id_reserva
        self.__id_morador = id_morador
        self.__data_reserva = data_reserva
        self.__area_reserva = area_reserva


    @property
    def id_reserva(self):
        return self.__id_reserva


    @id_reserva.setter
    def id_reserva(self, id_reserva):
        self.__id_reserva = id_reserva


    @property
    def id_morador(self):
        return self.__id_morador


    @id_morador.setter
    def id_morador(self, id_morador):
        self.__id_morador = id_morador


    @property
    def data_reserva(self):
        return self.__data_reserva


    @data_reserva.setter
    def data_reserva(self, data_reserva):
        self.__data_reserva = data_reserva
        
    @property
    def local_reserva(self):
        return self.__area_reserva
    
    @data_reserva.setter
    def local_reserva(self, area_reserva):
        self.__area_reserva = area_reserva