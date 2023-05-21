import requests as req
from files import send_email as se
import streamlit as st

api_key = "79d1f6c78da344299c31ce709ef97daf"

# UI
st.header("Receive 20 news about a topic you choose:")
st.subheader("Make sure to check your spam folder!")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address: ")
    topic = st.selectbox('Select a topic for the newsletter: ', ('Tesla', 'Business', 'Entertainment',
                                                                 'General', 'Health', 'Science', 'Sports',
                                                                 'Technology'))

    sub_btn = st.form_submit_button("Send")
    if sub_btn:
        # The URL for the news API
        url = f"https://newsapi.org/v2/everything?q={topic.lower()}&" \
              "from=2023-04-21&" \
              "sortBy=publishedAt&" \
              f"apiKey={api_key}&" \
              "language=en"

        try:
            # Make the API request
            response = req.get(url)
            content = response.json()

            # Construct the email body
            body = ""
            for article in content["articles"][:20]:
                if article.get("title"):
                    body += article["title"] + "\n" + article["description"] + "\n" + article["url"] + "\n\n"

            if body:
                message = f"Subject: {topic.capitalize()} News Letter\n\n{body}"
                se.send_email(message.encode("utf-8"), user_email)
                st.info("Email sent successfully!")
            else:
                st.warning("No articles found for the selected topic.")

        except req.RequestException as e:
            st.error(f"Error occurred while making the API request: {e}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
