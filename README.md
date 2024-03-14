# openai-voice-actor

This repository contains a simple yet powerful tool for converting text scripts into voice narrations using OpenAI's GPT model. The application is built with Streamlit, allowing for an easy-to-use interface where users can input their text and generate voice narrations in MP3 format. Whether you're creating content, need assistance with reading, or exploring text-to-speech technologies, this tool is designed to be accessible and straightforward.

## Features

- **Text Input**: Users can input any text script into the provided text area.
- **Voice Generation**: With the click of a button, the application generates a voice narration of the input text.
- **MP3 Download**: Users can download the generated narration as an MP3 file.

## Getting Started

To get started with the Text to Voice Converter, follow these steps:

### Prerequisites

- Python 3.9 or later
- An OpenAI API key

### Installation

1. **Clone the Repository**

2. **Set Up a Virtual Environment** (Optional but recommended)

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**

   Create a `.secrets.toml` file in the `.streamlit` directory of the project and add your OpenAI API key:

   ```plaintext
   OPENAI_API_KEY=your_openai_api_key_here
   ```

### Running the Application

After completing the installation steps, you can run the application using Streamlit:

```bash
streamlit run main.py
```

Open the link provided by Streamlit in your web browser, and you'll be greeted with the Text to Voice Converter interface.

### Using the Application

1. **Enter Your Text**: Type or paste the text you want to convert into the text area.
2. **Generate Voice**: Click the "Generate Voice" button to create the voice narration of your text.
3. **Download MP3**: After the voice has been generated, a download button will appear. Click it to download the MP3 file to your device.
