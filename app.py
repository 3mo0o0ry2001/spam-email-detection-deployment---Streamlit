import streamlit as st

# Create the welcome page
def welcome():
    st.title("Welcome for the first HTML Code.")

# Create the index page
def index():
    st.title("This is the second page.")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("Welcome", "Index"))

# Render the selected page
if page == "Welcome":
    welcome()
elif page == "Index":
    index()
