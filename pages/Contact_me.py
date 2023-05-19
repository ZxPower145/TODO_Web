import streamlit as st
from files.send_email import send_email

st.header("Contact me if you like my work :")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address: ")
    subject = st.text_input("Enter the subject: ")
    raw_message = st.text_area("Enter your message: ")
    message = f"""\
Subject: {subject}

From: {user_email}
{raw_message}
"""
    sub_btn = st.form_submit_button("Send")
    if sub_btn:
        send_email(message)
        st.info("Email sent successfully!")
