import streamlit as st
import math
from datetime import datetime
import time
bg_url = "./bg.png"
st.markdown(f"""
            <style>
            .stApp {{
            background-image: url("{bg_url}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            }}
            .block-container {{
            background: rgba(255,255,255,0.88);
            padding: 2rem;
            border-radius: 15px;
            }}
            </style>
            """, unsafe_allow_html=True)

st.title("Pie time! πππ")
clock_box = st.empty()
year_box = st.empty()
while True:
    now = datetime.now()
    decimal_hours = now.hour + now.minute/60 + now.second/3600 + now.microsecond/3600000/1000
    pi_time = decimal_hours / math.pi
    year_pi = now.year / math.pi
    clock_box.metric("Time now", f"{pi_time:.2f}π", now.strftime("%H:%M:%S"))
    year_box.metric("Year now", f"{year_pi:.2f}π", str(now.year))
    time.sleep(0.1) #or else it will go boom (?)

