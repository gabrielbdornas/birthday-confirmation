import os
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()

def call_supabase():
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    response = supabase.table("confirmations").select("*").execute()
    return response

if __name__== '__main__':
    response = call_supabase()
    print(response)
