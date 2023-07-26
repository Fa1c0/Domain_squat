import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

os.system('dnstwist -r yourcompany.org -f csv| cut -f 2 -d , > domains.txt')

connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

# Create the BlobServiceClient object
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

try:
    print("Uploading new file.")

    local_file_name = "domains.txt"

    # Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(container="domains", blob="domains.txt")

    # Delete old file
    blob_client.delete_blob()

    # Upload the new file
    with open(file="domains.txt", mode="rb") as data:
        blob_client.upload_blob(data)

except Exception as ex:
    print('Exception:')
    print(ex)
