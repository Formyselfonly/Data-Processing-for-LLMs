import json
import dotenv
import os
import cv2
from unstructured.partition.html import partition_html
from unstructured.partition.pptx import partition_pptx
from unstructured.staging.base import dict_to_elements, elements_to_json
from unstructured_client import UnstructuredClient
from unstructured_client.models import shared
from unstructured_client.models.errors import SDKError

# Pre-Step1.See https://docs.unstructured.io/api-reference/api-services/saas-api-development-guide#quick-start-example
# Pre-Step2. input the api_key and url in .env file

dotenv.load_dotenv()
API_KEY=os.getenv("UNSTRUCTURED_API_KEY")
API_URL=os.getenv("UNSTRUCTURED_API_URL")

unstructured_client = UnstructuredClient(
    api_key_auth=API_KEY,
    server_url=API_URL
)

html_demo_image=cv2.imread()