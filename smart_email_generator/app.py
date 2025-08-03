import streamlit as st
from openai import OpenAI
from fpdf import FPDF
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)
# ---------- CONFIGURATION ----------
st.set_page_config(page_title="Smart Email Generator", page_icon="📧", layout="centered")

st.markdown("""
    <style>
    body {
        background-color: #0e1117;
    }
    .stApp {
        background-color: #1e1f26;
        color: #e1e1e1;
        font-family: 'Segoe UI', sans-serif;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 0.6em 1.2em;
        font-size: 1em;
        border-radius: 5px;
    }
    .stSelectbox, .stTextArea {
        background-color: #2c2f35;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- APP UI ----------
st.markdown("""
    <h1 style='text-align: center;'>📧 Smart Email Generator</h1>
""", unsafe_allow_html=True)

tone = st.selectbox("Select tone", ["Formal", "Informal", "Professional", "Friendly"])
context = st.text_area("Enter context of the email")

client = OpenAI()

if st.button("Generate Email"):
    with st.spinner("Generating your email..."):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are an assistant that writes {tone.lower()} emails."},
                {"role": "user", "content": context}
            ]
        )
        email = response.choices[0].message.content
        st.session_state["generated_email"] = email
        st.success("Email generated!")
        st.markdown("---")
        st.markdown("### ✉️ Generated Email:")
        st.write(email)

# ---------- DOWNLOAD OPTIONS ----------
generated_email = st.session_state.get("generated_email", "")

if generated_email:
    # TXT
    st.download_button("📄 Download as TXT", generated_email, file_name="generated_email.txt")

    # PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in generated_email.split('\n'):
        pdf.cell(200, 10, txt=line, ln=True)

    pdf_path = "/tmp/generated_email.pdf"
    pdf.output(pdf_path)
    with open(pdf_path, "rb") as f:
        st.download_button("🧾 Download as PDF", f, file_name="generated_email.pdf")