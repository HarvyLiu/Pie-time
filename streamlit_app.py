import streamlit as st
import math
from datetime import datetime
import base64
from pathlib import Path

st.set_page_config(page_title="Pie time! πππ", layout="centered")
st.title("Pie time! πππ")
st.caption("Time and year displayed in π units — because why not?")

@st.fragment(run_every=0.1)
def pi_clock():
    now = datetime.now()
    decimal_hours = now.hour + now.minute/60 + now.second/3600 + now.microsecond/3600000000
    pi_time = decimal_hours / math.pi
    pi_year = now.year / math.pi
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Time now", f"{pi_time:.2f}π", now.strftime("%H:%M:%S"))
    with col2:
        st.metric("Year now", f"{pi_year:.2f}π", str(now.year))
pi_clock()

def get_base64_background(paths):
    for p in paths:
        if p.is_file():
            b64 = base64.b64encode(p.read_bytes()).decode("utf-8")
            mime = "image/jpeg" if p.suffix==".jpg" else "image/png"
            return b64, mime
    return None

bg_result = get_base64_background([Path("bg.jpg")])
# Bellow is written in AI cause I'm not really good at CSS
"""Next time when your friends ask you for the time, just answer it in πs"""
if bg_result:
    b64_data, mime = bg_result
    st.markdown(f"""
        <style>
        .stApp {{ background-image: url("data:{mime};base64,{b64_data}"); background-size: cover; }}
        .block-container {{ background: rgba(255,255,255,0.88); padding: 2rem; border-radius: 15px; }}
        </style>
        """, unsafe_allow_html=True)
else:
    st.markdown("""<style>.block-container { background: rgba(255,255,255,0.88); }</style>""", unsafe_allow_html=True)


