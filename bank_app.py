import streamlit as st
import pandas as pd

def login_page():
    st.title("Banking Application")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Submit"):
        if username == "admin" and password == "Passkey":
            st.success("Login Successful")
            st.session_state.logged_in = True
            st.session_state.current_page = "home"
        else:
            st.error("Invalid username or password")

def session1():
    st.title("Banking Application")
    st.header("Session 1")
    st.button("Logout", on_click=logout)

def session2():
    st.title("Banking Application")
    st.header("Session 2")

    def load_data():   
        df = pd.read_csv("customer_data.csv")
        return df

    if st.button("Total Users"):
        df = load_data()
        st.write(df)
    st.button("Logout", on_click=logout)

def main():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        if "current_page" not in st.session_state:
            st.session_state.current_page = "home"

        if st.session_state.current_page == "home":
            st.write("Banking Application")
            st.button("Logout", on_click=logout)
            if st.sidebar.button("Session 1"):
                st.session_state.current_page = "session1"
            if st.sidebar.button("Session 2"):
                st.session_state.current_page = "session2"
        elif st.session_state.current_page == "session1":
            session1()
        elif st.session_state.current_page == "session2":
            session2()
    else:
        login_page()

def logout():
    st.session_state.logged_in = False
    st.session_state.current_page = "home"

if __name__ == "__main__":
    main()
