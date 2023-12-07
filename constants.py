from dotenv import load_dotenv
import os
load_dotenv()

class Config:
	api_key = os.environ.get('CUSTOMGPT_API_KEY')
	base_url = os.environ.get('CUSTOMGPT_BASE_URL') or "https://app.customgpt.ai"
	project_id = os.environ.get('CUSTOMGPT_PROJECT_ID')


