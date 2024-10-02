"""
Modulo TicketFinder
Author: @C4mdax
Version 1.0

"""

import csv

class TicketFinder:
    '''
    Clase TicketFinder. Encuentra un ticket en el archivo csv_file

    Metodos
    -------
    * __init__(csv_file)
    * read_ticket (ticket_id)

    Atributos
    -------
    * csv_file (str): Dirección del archivo csv donde se realizará la busqueda
    
    '''

    def __init__(self, csv_file):
        """
        Metodo contructor de TicketFinder
        
        Atributos:
        * csv_file (str):  Dirección del archivo csv donde se realizará la busqueda
        
        """
        self.csv_file = csv_file

    def read_ticket(self, ticket_id):
        """
        Metodo read_ticket.

        Atributos:
        * ticket_id (int): Numero de vuelo

        Returns:
        * iatas (list): Lista con los 2 códigos iatas a buscar
        """
        iatas = []
        with open(self.csv_file, mode='r', encoding = 'utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['ticket_id'] == str(ticket_id):
                    origin = row['origin']
                    destination = row['destination']
                    iatas.append(origin)
                    iatas.append(destination)
                    return iatas
            return "Ticket de vuelo no encontrado"


            

