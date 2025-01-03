import streamlit as st

def main():
    st.title("Birthday Party Confirmation")

    with st.form("confirmation_form"):
        # Sponsor's name
        sponsor_name = st.text_input("Your Name", placeholder="Enter your name", key="sponsor_name")

        # Number of people
        num_people = st.number_input("Number of people coming with you (including yourself):", min_value=1, step=1, key="num_people")

        # Dynamic fields for names based on the number of people
        person_names = []
        for i in range(num_people):
            name = st.text_input(f"Name of Person {i + 1}", placeholder=f"Enter the name of person {i + 1}", key=f"person_{i}")
            person_names.append(name)

        # Submit button
        submitted = st.form_submit_button("Submit")

        # Handle form submission
        if submitted:
            if not sponsor_name.strip():
                st.error("Please enter your name.")
            elif any(not name.strip() for name in person_names):
                st.error("Please make sure all names are filled in.")
            else:
                st.success("Thank you for your confirmation!")
                st.write(f"**Confirmation from:** {sponsor_name}")
                st.write("**People confirmed:**")
                for i, name in enumerate(person_names, start=1):
                    st.write(f"{i}. {name}")

if __name__ == "__main__":
    main()
