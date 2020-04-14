import csv
from clients.models import Client
import os


class ClientService:
    def __init__(self, table_name):
        self.table_name = table_name
    
    def create_client(self, client):
        with open(self.table_name, mode='a') as f:
            writer = csv.DictWriter(f, fieldnames= Client.schema())
            writer.writerow(client.to_dict())
    

    def list_clients(self):
        with open(self.table_name, mode='r') as f:
            reader = csv.DictReader(f, fieldnames= Client.schema())

            return list(reader)


    def update_client(self,  updated_client ):
        clients = self.list_clients()

        updated_clients = list()

        for cli in clients:
            if cli['uid'] == updated_client.uid:
                updated_clients.append(updated_client.to_dict())
            else:
                updated_clients.append(cli)
        
        self._save_to_disk(updated_clients)


    def delete_client(self, uid):
        clients = self.list_clients()

        updated_clients = list()

        for cli in clients:

            if cli['uid'] == uid:
                pass
            else:
                updated_clients.append(cli)
        
        self._save_to_disk(updated_clients)

    

    def _save_to_disk(self, clients):
        temp_table_name = self.table_name + '.tmp'
        with open(temp_table_name, mode='w') as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            writer.writerows(clients)

        os.remove(self.table_name)
        os.rename(temp_table_name, self.table_name)

    



