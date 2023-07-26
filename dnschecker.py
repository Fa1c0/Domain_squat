import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

print('Creating new domains.txt list.')

os.system('dnstwist -r wolfspeed.com -f csv| cut -f 2 -d , > domains.txt')

connect_str = ('DefaultEndpointsProtocol=https;AccountName=dnstwist;AccountKey=lA+W+XSM6XKD87RGOUK5F7JBgVyB+QmldBVawj1G0pE5sYHdofiKMf2zSMUHQXMygizwYUW+Yay/+ASt0CJLwQ==;EndpointSuffix=core.windows.net')

# Create the BlobServiceClient object
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

try:
    # Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(container="domains", blob="domains.txt")

    # Delete old file
    blob_client.delete_blob()

    # Upload the new file
    with open(file="domains.txt", mode="rb") as data:
        blob_client.upload_blob(data)

    print('Old file deleted and replacment uploaded.')

except Exception as ex:
    print('Exception:')
    print(ex)
