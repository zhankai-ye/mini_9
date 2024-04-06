import streamlit as st
from transformers import pipeline

# Load the language model
model = pipeline("text-generation", model="openai-gpt")

# Define Streamlit app with enhanced aesthetics, additional content, and fancy styling
def main():
    # Set page title and add some custom styling
    st.set_page_config(
        page_title="AI Text Generator",
        page_icon="🌌",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Customize CSS for the app
    st.markdown("""
    <style>
    /* Main page styling */
    .stApp {
        background-color: #343a40;
    }
    
    /* Header styling */
    header {
        background-color: #007bff;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 20px;
    }
    
    h1 {
        color: #ffffff;
        text-align: center;
        font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
    }
    
    /* Introduction section styling */
    .intro {
        background-color: #6c757d;
        padding: 20px;
        border-radius: 15px;
        color: #ffffff;
        margin-bottom: 20px;
    }
    
    .intro p {
        font-family: Arial, sans-serif;
    }
    
    .stButton>button {
        color: #ffffff;
        background-color: #007bff;
        border-radius: 20px;
        border: 1px solid #007bff;
        font-size: 20px;
        font-weight: bold;
        padding: 10px 24px;
    }
    
    .stTextArea>div>div>textarea {
        background-color: #ffffff;
        color: #343a40;
        font-size: 18px;
        border-radius: 20px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Add header with image
    st.markdown("""
    <header>
        <h1>🌌 AI Text Generator App</h1>
    </header>
    """, unsafe_allow_html=True)
    
    # Add introduction section
    st.markdown("""
    <div class="intro">
        <p>Welcome to the AI Text Generator app powered by Streamlit and Hugging Face Transformers!</p>
        <p>This app showcases the capabilities of a leading-edge language model for text generation.</p>
        <p>Type in some text below, hit <strong>Generate</strong>, and let the model extend your text. Explore various prompts and discover the creative outputs you can achieve!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Add text input area with placeholder
    text_input = st.text_area("Enter text here to generate continuation...", height=150)
    
    # Add generate button with custom styling
    if st.button("Generate", key="generate_button"):
        if text_input:
            # Generate text with the language model
            generated_text = model(text_input, max_length=50, do_sample=True)[0]['generated_text']
            
            # Display generated text with styling
            st.markdown(f"""
            <div style="background-color: #007bff; color: white; padding: 20px; border-radius: 10px; margin-top: 20px;">
                <h2>Generated Text</h2>
                <p>{generated_text}</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            # Display warning if no text input
            st.warning("Please enter some text to generate.")

if __name__ == "__main__":
    main()
