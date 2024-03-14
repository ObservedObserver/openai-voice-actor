import streamlit as st
from openai import OpenAI

st.title("Openai Voice Actor")

api_key = None
try:
    api_key = st.secrets["OPENAI_API_KEY"]
except:
    pass

if api_key is None:
    api_key = st.text_input("Set your own openai key", type="password")

client = OpenAI(api_key=api_key)


voice_option = st.selectbox(
    "Voice Options", ("onyx", "alloy", "echo", "fable", "nova", "shimmer")
)

model_option = st.selectbox("Model", ("tts-1", "tts-1-hd"))
user_input = st.text_area("Enter the text you want to convert to speech:", height=300)

if st.button("Convert to Speech"):
    if user_input:
        response = client.audio.speech.create(
            model=model_option,
            voice=voice_option,
            input=user_input,
        )

        with st.spinner("Generating voice..."):
            audio_file = "output.mp3"
            response.stream_to_file(audio_file)

            audio_bytes = open(audio_file, "rb").read()
            st.audio(audio_bytes, format="audio/mp3", start_time=0)

            st.download_button(
                label="Download Speech",
                data=audio_bytes,
                file_name="output.mp3",
                mime="audio/mp3",
            )
    else:
        st.write("Please enter some text to convert to speech.")
