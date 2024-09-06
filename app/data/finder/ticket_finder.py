import csv

class TicketFinder:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def read_ticket(self, ticket_id):
        with open(self.csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['ticket_id'] == str(ticket_id):
                    return f"Origin: {row['origin']}, Destination: {row['destination']}"
                return "Ticket de vuelo no encontrado."


            

