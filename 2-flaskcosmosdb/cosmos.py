import azure.cosmos.documents as cosmos
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey
import config

HOST = config.settings['host']
MASTER_KEY = config.settings['master_key']
DATABASE_ID = config.settings['database_id']

def connect():
    client = cosmos_client.CosmosClient(
        HOST, 
        {'masterKey': MASTER_KEY}, 
        user_agent="CosmosDBPythonQuickstart", 
        user_agent_overwrite=True
    )
    
    try:
        db = client.create_database(id=DATABASE_ID)
    except exceptions.CosmosResourceExistsError:
        db = client.get_database_client(DATABASE_ID)
    finally:
        return db

def get_container(name, connection):
    try:
        container = connection.create_container(id=name, partition_key=PartitionKey(path='/partitionKey'))
    except exceptions.CosmosResourceExistsError:
        container = connection.get_container_client(name)
    finally:
        return container




def get_all(container):
    items = list(container.read_all_items(max_item_count=10))
    return items

def get_one(container, id, partitionKey):
    item = container.read_item(item=id, partition_key=partitionKey)
    return item


def insert_one(container, item):
    container.create_item(body=item)