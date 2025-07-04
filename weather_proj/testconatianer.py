import os
import json
from azure.storage.blob import BlobServiceClient
import datetime

def write_to_azure_blob(data: dict) -> str:
    blob_conn_str = "DefaultEndpointsProtocol=https;AccountName=weatherraw25;AccountKey=k9dFJHtS3ZKrOwdY91ETEmNnUfLZotS25781iumemfDGfsxv5olQA8KyTpTdNDOdj3Iq8s7Trqpp+ASteaFlAQ==;EndpointSuffix=core.windows.net"
    if not blob_conn_str:
        raise ValueError("AZURE_STORAGE_CONNECTION_STRING is not set.")

    container = "rawweatherdata"
    file_name = f"test-weather-{datetime.date.today()}.json"

    blob_service = BlobServiceClient.from_connection_string(blob_conn_str)

    # Create the container if it doesn't exist
    try:
        blob_service.create_container(container)
        print(f"Container '{container}' created.")
    except Exception as e:
        # Ignore error if it already exists
        if "ContainerAlreadyExists" not in str(e):
            raise

    blob_client = blob_service.get_container_client(container).get_blob_client(file_name)
    blob_client.upload_blob(json.dumps(data), overwrite=True)
    print(f"Wrote test blob: {file_name}")
    return file_name

if __name__ == "__main__":
    test_data = {"test": "this is test data", "value": 123}
    write_to_azure_blob(test_data)
