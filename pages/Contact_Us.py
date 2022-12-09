import streamlit as st
import pandas
from send_mail import send_email

df = pandas.read_csv("topics.csv")
topics = [row['topic'] for index, row in df.iterrows()]
st.header("Contact Us")
with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    discussion_topic = st.selectbox("What topic do you want to discuss?", topics)
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
Topic {discussion_topic}
{raw_message}
"""
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        send_email(message)
        st.info("Your email was sent successfully!")