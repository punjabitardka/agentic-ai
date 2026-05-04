import os 
from dotenv import load_dotenv

load_dotenv()

serp_key = os.getenv("SERP_API_KEY")
search_key = os.getenv("SEARCH_API_KEY")
IMGBB_KEY = os.getenv("IMGBB_KEY")


