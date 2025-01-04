from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

def init_supabase():
    SUPABASE_URL = os.environ.get("SUPABASE_URL")
    SUPABASE_KEY = os.environ.get("SUPABASE_KEY")
    return create_client(SUPABASE_URL, SUPABASE_KEY)

def save_to_supabase(supabase: Client, st, sponsor_name, acompanhantes, person_names):
    try:
        data = {
            "sponsor_name": sponsor_name,
            "total_convidados": acompanhantes + 1,
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

# Function to get the total number of confirmed people
def get_total_confirmed_people():
    supabase = init_supabase()
    try:
        # Query the Supabase table
        response = supabase.table("confirmations") \
            .select("id, total_convidados, env") \
            .neq("env", "DEV") \
            .execute()

        # Check for errors
        if type(response.data[0]['id']) != int:
            raise Exception(f"Error fetching data: {response.json()}")

        # Sum the total_convidados column
        total_people = sum(row["total_convidados"] for row in response.data)
        return total_people
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

# Function to get the total drinks
def get_total_drinks():
    supabase = init_supabase()
    try:
        # Query the Supabase table
        response = supabase.table("confirmations") \
            .select("id, bebidas, env") \
            .neq("env", "DEV") \
            .execute()

        # Check for errors
        if type(response.data[0]['id']) != int:
            raise Exception(f"Error fetching data: {response.json()}")

        # Sum the total_convidados column
        # breakpoint()
        # bebidas = [data['bebidas'] for data in response.data]
        # return total_people
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

# if __name__== '__main__':
#     get_total_confirmed_people()
