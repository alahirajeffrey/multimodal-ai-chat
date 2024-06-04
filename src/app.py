import streamlit as st


def clear_input_field():
    """
    save user's input to session state and clear test input holding the user's input
    """
    st.session_state.user_question = st.session_state.user_input
    st.session_state.user_input =""

def send_input_changed():
    """
    set send input session state to true and call clear input field function
    """
    st.session_state.send_input = True
    clear_input_field()
    
def set_sidebar(streamlit_object):
    """
    function to setup sidebar to allow upload of audio, image and pdf
    """
    upload_audio = streamlit_object.sidebar.file_uploader("Upload audio", type=["wav", "mp3"])
    upload_image = streamlit_object.sidebar.file_uploader("Upload image",  type=["jpg", "jpeg", "png"])
    upload_pdf = streamlit_object.sidebar.file_uploader("Upload pdf file", type=["pdf"])

    return (upload_audio, upload_image, upload_pdf)
    

def main():
    st.title("Multimodal Chat Application")
    chat_container = st.container()

    #  call function to set side bar and return media objects
    uploaded_audio, uploaded_image, uploaded_pdf = set_sidebar(st)

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

