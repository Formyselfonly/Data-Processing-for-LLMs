import json
import dotenv
import os
from unstructured.partition.html import partition_html
from unstructured.partition.ppt import partition_ppt
from unstructured.partition.pdf import partition_pdf
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

#There are three main types which are:html,ppt,pdf
# We pre-processing them into json format to normalizaiton

# Step1. unstructured data processing
winter_sport_file="../resources/winter_sports.pdf"
winter_sport_elements=partition_pdf(filename=winter_sport_file)
winter_sport_element_dict=[e.to_dict() for e in winter_sport_elements]
example_output=json.dump(winter_sport_element_dict[:],indent=3)


# Step2.See the structure of the winter_sport_file and than choose meethod to process
print(example_output)

# Step3.Find elements associated with chapters
# To be written
# Step4.Load documents into a vector db
# To be written
# Step5.peek&search&chunking content in vector db
# To be written
