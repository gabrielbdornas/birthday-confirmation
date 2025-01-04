from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

def init_supabase():
    SUPABASE_URL = os.environ.get("SUPABASE_URL")
    SUPABASE_KEY = os.environ.get("SUPABASE_KEY")
    return create_client(SUPABASE_URL, SUPABASE_KEY)

def save_to_supabase(supabase: Client, st, sponsor_name, sponsor_email, num_people, person_names):
    try:
        data = {
            "sponsor_name": sponsor_name,
            "sponsor_email": sponsor_email,
            "num_people": num_people,
            "person_names": person_names,
            "env": os.environ.get("ENV"),
        }
        response = supabase.table("confirmations").insert(data).execute()
        if type(response.data[0]['id']) == int:
            return True
        else:
            st.error(f"Falha para salvar sua resposta: {response.json()}")
            return False
    except Exception as e:
        st.error(f"Algum erro aconteceu: {e}")
        return False
