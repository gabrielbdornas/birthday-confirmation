import streamlit as st
from supabase_conection import init_supabase, save_to_supabase

def remove_streamlit_hamburguer():
    hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)


def main():

    st.set_page_config(
        page_title="Gabriel 40 Anos - Confirme presença nesta festança",
        page_icon=":beers:",
        menu_items={}  # Disable the hamburger menu
    )

    remove_streamlit_hamburguer()

    st.title(":tada: Gabriel 40 Anos! :beers:")

    st.write(f"**Confirme presença nesta festança**")

    supabase = init_supabase()

    # Sponsor's name
    sponsor_name = st.text_input("Convidado:", placeholder="Preencha seu nome!", key="sponsor_name")

    # Number of people
    acompanhantes = st.number_input("Convidado(s) Acompanhante(s):", min_value=0, step=1, key="acompanhantes")

    # Dynamic fields for names based on the number of people
    person_names = []
    for i in range(acompanhantes):
        name = st.text_input(f"Nome do {i + 1}° acompanhante:", placeholder=f"Nome da {i + 1}° acompanhante", key=f"person_{i}")
        person_names.append(name)

    # Submit button
    submitted = st.button("Enviar")

    # Handle form submission
    if submitted:
        if not sponsor_name.strip():
            st.error("Por favor, preencha seu nome.")
        elif any(not name.strip() for name in person_names):
            st.error("Por favor, preencha todos os nomes.")
        else:
            if save_to_supabase(supabase, st, sponsor_name, acompanhantes, person_names):
                st.success(f"Obrigado pela sua confirmação {sponsor_name}!")
                if acompanhantes > 0:
                    st.write(f"**Acompanhantes:**")
                    for i, name in enumerate(person_names, start=1):
                        st.success(f"{i}. {name}")

if __name__ == "__main__":
    main()
