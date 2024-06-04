import streamlit as st

def clear_input_field():
    st.session_state.user_question = st.session_state.user_input
    st.session_state.user_input =""

def send_input_changed():
    st.session_state.send_input = True
    clear_input_field()
    

def main():
    st.title("Multimodal Chat Application")
    chat_container = st.container()

    if "send_input" not in st.session_state:
        st.session_state.send_input = False
        st.session_state.user_question = ""

    user_input = st.text_input("Type your message here", key="user_input", on_change=send_input_changed)
    send_button = st.button("Send", key="send_button")

    if send_button or st.session_state.send_input:
        if st.session_state.user_question != "":
            llm_response = ("This is a generic response")

            with chat_container:
                st.chat_message("user").write(st.session_state.user_question)
                st.chat_message("ai").write(llm_response)

if __name__ == "__main__":
    main()

