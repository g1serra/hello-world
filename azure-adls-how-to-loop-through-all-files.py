"""
goto -> azure > adls2source > Security + networking > Access keys > Connection string
"""
CONNECTION_STRING = CONNECTION_STRING

import os
import sys

from azure.storage.blob import BlobServiceClient
from azure.storage.blob import BlobPrefix

try:
    CONNECTION_STRING = CONNECTION_STRING
except KeyError:
    print("AZURE_STORAGE_CONNECTION_STRING must be set.")
    sys.exit(1)

def walk_container(client, container):
    container_client = client.get_container_client(container.name)
    print('container -> {}'.format(container.name))
    depth = 1
    separator = '   '

    def walk_blob_hierarchy(prefix=""):
        nonlocal depth
        for item in container_client.walk_blobs(name_starts_with=prefix):
            short_name = item.name[len(prefix):]
            if isinstance(item, BlobPrefix):
                print('folder    -> ' + separator * depth + short_name)
                depth += 1
                walk_blob_hierarchy(prefix=item.name)
                depth -= 1
            else:
                message = 'file      ->' + separator * depth + short_name
                results = list(container_client.list_blobs(name_starts_with=item.name, include=['snapshots']))
                num_snapshots = len(results) - 1
                if num_snapshots:
                    message += " ({} snapshots)".format(num_snapshots)
                print(message)
    walk_blob_hierarchy()

try:
    service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
    containers = service_client.list_containers()
    for container in containers:
        walk_container(service_client, container)
except Exception as error:
    print(error)
    sys.exit(1)