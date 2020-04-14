import click
from clients.services import ClientService
from clients.models import Client


@click.group()
def clients():
    """Manages the clients lifecycle"""
    pass


@clients.command()
@click.option('-n', 
            '--name', 
            type=str,
            prompt=True,
            help = 'The client name')
@click.option('-c', 
            '--company', 
            type=str,
            prompt=True,
            help = 'The client company')
@click.option('-e', 
            '--email', 
            type=str,
            prompt=True,
            help = 'The client email') 
@click.option('-p', 
            '--position', 
            type=str,
            prompt=True,
            help = 'The client position')          
@click.pass_context
def create(ctx, name, company, email, position):
    """Create a new client"""
    client = Client(name, company, email, position)
    client_service = ClientService(ctx.obj['clients_table'])

    client_service.create_client(client)
    


@clients.command()
@click.pass_context
def list(ctx):
    """List all clients"""

    
    client_service = ClientService(ctx.obj['clients_table'])
    
    clients_list = client_service.list_clients()

    click.echo('ID  |  name  |  company  |  email  |  position')
    click.echo('*'*50)

    for client in clients_list:
        click.echo('{} | {} | {} | {} | {}'.format(client['uid'], client['name'], client['company'], client['email'],client['position'] ))
    


@clients.command()
@click.argument('client_uid',
            type=str) 
@click.pass_context
def update(ctx, client_uid):
    """updates a client"""
    client_service = ClientService(ctx.obj['clients_table'])


    client_list = client_service.list_clients()

    client = [client for client in client_list if client['uid'] == client_uid]
    
    if client:
        client = _update_client_flow(Client(**client[0]))
        client_service.update_client(client)

        click.echo('client successfully updated')
    else:
        click.echo('client not found')



def _update_client_flow(updated_client):
    click.echo('leave empty if dont want to modify the values')

    updated_client.name = click.prompt('New Name', type=str, default=updated_client.name)
    updated_client.company = click.prompt('New company', type=str, default=updated_client.company)
    updated_client.email = click.prompt('New email', type=str, default=updated_client.email)
    updated_client.position = click.prompt('New position', type=str, default=updated_client.position)

    return updated_client
    

@clients.command()
@click.argument('client_uid',
            type=str) 
@click.pass_context
def delete(ctx, client_uid):
    """delete a client"""
    client_service = ClientService(ctx.obj['clients_table'])

    client_list = client_service.list_clients()

    deleted_client = [client for client in client_list if client['uid'] == client_uid]

    if deleted_client:
        client_service.delete_client(client_uid)
        click.echo('client successfully deleted')
    else:
        click.echo('client not found')



all = clients

