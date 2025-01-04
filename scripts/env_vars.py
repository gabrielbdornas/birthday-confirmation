import os
from dotenv import load_dotenv

load_dotenv()

ENV = os.environ.get("ENV")
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")
