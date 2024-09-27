import json
import dotenv
import os
from unstructured.partition.html import partition_html
from unstructured.partition.ppt import partition_ppt
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

# Type1.html unstructured data processing
html_file="../resources/medium_blog.html"
html_elements=partition_html(filename=html_file)
html_element_dict=[e.to_dict() for e in html_elements]
example_output=json.dump(html_element_dict[10:14],indent=3)
print(example_output)

# Type2.ppt unstructured data processing
ppt_file="../resources/msft_openai.pptx"
ppt_elements=partition_ppt(filename=ppt_file)
ppt_element_dict=[e.to_dict() for e in ppt_elements]
example_output=json.dump(ppt_element_dict[:],indent=3)

# Type3.pdf unstructured data processing