import wikipedia
import streamlit as st

# Set user-agent as required by Wikipedia's terms
wikipedia.set_user_agent('TalkEazy/1.0 (contact: jjj907269@gmail.com)')

# Title of the app
st.title("TalkEazy: Your AI-powered Assistant")

# Input box for the user to ask a question
user_input = st.text_input("Ask anything:")

# If user input is given
if user_input:
    try:
        # Fetch the summary of the question from Wikipedia
        answer = wikipedia.summary(user_input, sentences=3)
        st.write("Answer:", answer)
    except wikipedia.exceptions.DisambiguationError as e:
        st.write("The query is ambiguous. Here are some suggestions:")
        st.write(e.options)
    except wikipedia.exceptions.HTTPTimeoutError:
        st.write("Timeout error. Please try again later.")
    except wikipedia.exceptions.RequestException as e:
        st.write(f"An error occurred: {e}")