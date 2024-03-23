from dotenv import load_dotenv
import os

load_dotenv(verbose=True)

USERNAME = os.getenv("DANBOORU_USERNAME")
API_KEY = os.getenv("API_KEY")