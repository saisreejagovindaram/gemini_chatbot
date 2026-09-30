import os
from google import genai
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

st.set_page_config(
    page_title="Gemini AI Chatbot", page_icon="🤖", layout="centered"
)

# Custom CSS with fix for scrolling long content
st.markdown(
    """
    <style>
    /* 1. App background pattern & gradients */
    .stApp {
        background-color: #f5f2eb !important;
        background-image: 
            radial-gradient(at 10% 20%, rgba(217, 119, 6, 0.08) 0px, transparent 50%),
            radial-gradient(at 90% 80%, rgba(180, 83, 9, 0.08) 0px, transparent 50%),
            radial-gradient(at 50% 50%, rgba(235, 220, 219, 0.4) 0px, transparent 70%),
            url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E") !important;
        color: #2d2b2a !important;
        font-family: 'Inter', sans-serif;
    }

    /* 2. Enable normal scrolling on outer page container */
    [data-testid="stMain"] {
        display: flex !important;
        flex-direction: column !important;
        min-height: 100vh !important;
    }

    /* 3. Center card while maintaining top/bottom margin scrolling */
    .block-container {
        background: rgba(247, 245, 240, 0.85);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        border-radius: 20px;
        padding: 2.5rem 2rem !important;
        border: 1px solid rgba(212, 206, 203, 0.6);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.05);
        max-width: 650px !important;
        width: 100% !important;
        margin: auto !important; /* Centers card vertically without hiding top overflow */
    }

    /* Title Styling */
    h1 {
        color: #362f2d !important;
        font-weight: 800 !important;
        text-align: center;
        padding-bottom: 0.3rem;
    }

    /* Subtitle styling */
    .stMarkdown p {
        color: #5a5450;
    }

    /* Input text area styling */
    .stTextArea textarea {
        background-color: #eae6df !important;
        color: #2d2b2a !important;
        border: 1px solid #d4cecb !important;
        border-radius: 12px !important;
        padding: 12px !important;
        font-size: 16px !important;
    }
    .stTextArea textarea:focus {
        border-color: #7a6e67 !important;
        box-shadow: 0 0 0 2px rgba(122, 110, 103, 0.2) !important;
    }

    /* Text area label */
    .stTextArea label {
        color: #362f2d !important;
        font-weight: 600 !important;
    }

    /* Button styling */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #d97706 0%, #b45309 100%) !important;
        color: #ffffff !important;
        border: none !important;
        padding: 0.75rem 1.5rem !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        border-radius: 10px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 10px rgba(180, 83, 9, 0.2);
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(180, 83, 9, 0.35);
        background: linear-gradient(135deg, #b45309 0%, #92400e 100%) !important;
    }

    /* Response output card with internal scroll capability if needed */
    .response-card {
        background-color: #ebdcdb !important;
        border-left: 5px solid #d97706;
        color: #2d2b2a !important;
        padding: 1.25rem;
        border-radius: 10px;
        margin-top: 1rem;
        line-height: 1.6;
        font-size: 15px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.02);
    }
    </style>
""",
    unsafe_allow_html=True,
)

st.title("Gemini AI Chatbot")
st.write("Ask Gemini anything!")

prompt = st.text_area(
    "Enter your prompt:",
    placeholder="Explain Artificial Intelligence in simple words",
    height=120,
)

if st.button("Generate Response"):
    if prompt:
        with st.spinner("Gemini is thinking..."):
            response = client.models.generate_content(
                model="gemini-3.5-flash-lite", contents=prompt
            )
        st.success("Response generated!")

        st.markdown(
            f'<div class="response-card">{response.text}</div>',
            unsafe_allow_html=True,
        )
    else:
        st.warning("Please enter a prompt.")