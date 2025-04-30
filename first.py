


x=1
y=2
print (x+y)
import streamlit as st
import time

# This gets the user’s email if app access is restricted
user_email = st.experimental_user.email if st.experimental_user else "unknown"

# Log to a file or database
with open("access_logs.txt", "a") as f:
    f.write(f"{time.ctime()} - Accessed by: {user_email}\n")
