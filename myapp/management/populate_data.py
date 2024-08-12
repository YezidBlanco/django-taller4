from django.core.management.base import BaseCommand
from myapp.models import Partido, Presidente


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        data = [
            ["1", "José María Campo Serrano", "1886", "1887", "Partido Nacional"],
            ["2", "Eliseo Payán Hurtado", "1887", "1887", "Partido Nacional"],
            ["3", "Rafael Nuñez Moledo", "1887", "1888", "Partido Nacional"],
            ["4", "Carlos Holguín Mallarino", "1888", "1892", "Partido Nacional"],
            ["4", "Miguel Antonio Caro", "1892", "1892", "Partido Nacional"],
            ["5", "Rafael Nuñez Moledo", "1892", "1894", "Partido Nacional"],
            ["5", "Antonio Basilio Cuervo", "1893", "1893", "Partido Conservador"],
            ["6", "Miguel Antonio Caro", "1894", "1898", "Partido Nacional"],
            ["6", "Guillermo Quintero Calderón", "1896", "1896", "Partido Conservador"],
            ["7", "Manuel Antonio Sanclemente", "1898", "1900", "Partido Nacional"],
            ["8", "José Manuel Marroquin", "1900", "1904", "Partido Conservador"],
            ["9", "Rafael Reyes Prieto", "1904", "1909", "Partido Conservador"],
            ["9", "Diego Euclides de Angulo Lemos (interino)", "1908", "1908", "Partido Conservador"],
            ["10", "Jorge Holguin Mallarino", "1909", "1909", "Partido Conservador"],
            ["11", "Ramón González Valencia", "1909", "1910", "Partido Conservador"],
            ["12", "Carlos Eugenio Restrepo", "1910", "1914", "Unión Republicana(Conservador)"],
            ["13", "José Vicente Concha", "1914", "1918", "Partido Conservador"],
            ["14", "Marco Fidel Suárez", "1918", "1921", "Partido Conservador"],
            ["15", "Jorge Holguín Mallarino", "1921", "1922", "Partido Conservador"],
            ["16", "Pedro Nel Ospina", "1922", "1926", "Partido Conservador"],
            ["17", "Miguel Abadía Méndez", "1926", "1930", "Partido Conservador"],
            ["18", "Enrique Olaya Herrera", "1930", "1934", "Partido Liberal"],
            ["19", "Alfonso López Pumarejo", "1934", "1938", "Partido Liberal"],
            ["20", "Eduardo Santos Montejo", "1938", "1942", "Partido Liberal"],
            ["21", "Alfonso López Pumarejo", "1942", "1945", "Partido Liberal"],
            ["21", "Carlos Lozano y Lozano", "1942", "1942", "Partido Liberal"],
            ["21", "Darío Echandía Olaya", "1943", "1944", "Partido Liberal"],
            ["22", "Alberto Lleras Camargo", "1945", "1946", "Partido Liberal"],
            ["23", "Mariano Ospina Pérez", "1946", "1950", "Partido Conservador"],
            ["24", "Laureano Gómez Castro", "1950", "1951", "Partido Conservador"],
            ["25", "Roberto Urdaneta Arbelaez", "1951", "1953", "Partido Conservador"],
            ["26", "Gustavo Rojas Pinilla", "1953", "1957", "Militar"],
            ["27", "Junta Militar de Gobierno", "1957", "1958", "Militar"],
            ["28", "Alberto Lleras Camargo", "1958", "1962", "Partido Liberal"],
            ["29", "Guillermo León Valencia", "1962", "1966", "Partido Conservador"],
            ["29", "José Antonio Montalvo", "1963", "1963", "Partido Conservador"],
            ["30", "Carlos Lleras Restrepo", "1966", "1970", "Partido Liberal"],
            ["31", "Misael Pastrana Borrero", "1970", "1974", "Partido Conservador"],
            ["31", "Rafael Azuero Manchola", "1973", "1973", "Partido Conservador"],
            ["32", "Alfonso López Michelsen", "1974", "1978", "Partido Liberal"],
            ["32", "Indalecio Liévano Aguirre", "1976", "1976", "Partido Liberal"],
            ["33", "Julio César Turbay Ayala", "1978", "1982", "Partido Liberal"],
            ["33", "Víctor Mosquera Chaux", "1981", "1981", "Partido Liberal"],
            ["34", "Belisario Betancur Cuartas", "1982", "1986", "Partido Conservador"],
            ["35", "Virgilio Barco Vargas", "1986", "1990", "Partido Liberal"],
            ["36", "César Gaviria Trujillo", "1990", "1994", "Partido Liberal"],
            ["37", "Ernesto Samper Pizano", "1994", "1998", "Partido Liberal"],
            ["38", "Andrés Pastrana Arango", "1998", "2002", "Partido Conservador"],
            ["39", "Álvaro Uribe Vélez", "2002", "2010", "Partido Primero Colombia"],
            ["40", "Juan Manuel Santos Calderón", "2010", "2018", "Partido de la U"],
            ["41", "Iván Duque Márquez", "2018", "2022", "Partido Centro Democrático"],
            ["42", "Gustavo Francisco Petro Urrego", "2022", "2026", "Colombia Humana"],
        ]

        for registro in data:
            numero = registro[0]
            nombre = registro[1]
            f_inicio = registro[2]
            f_fin = registro[3]
            partido = registro[4]
            
        
            partido_obj = Partido.objects.filter(name=partido).first()
            if not partido_obj:
                partido_obj = Partido(
                    name=partido,
                    description="1234679"
                )
                partido_obj.save()
                
            presidente = Presidente.objects.filter(name=nombre).first()
            if not presidente:
                presidente = Presidente(
                    numero=numero,
                    name=nombre,
                    partido=partido_obj,
                    inicio=f_inicio,
                    final=f_fin,
                    description='12346',
                )
                presidente.save()