import streamlit as st


def main():
    st.title("Multimodal Chat Application")

    user_input = st.text_input("Type your message here", key="user_input")
    send_button = st.button("Send", key="send_button")

    if send_button:
        llm_response = ("This is a generic response")

if __name__ == "__main__":
    main()

