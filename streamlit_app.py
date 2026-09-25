import streamlit as st
import math
from datetime import datetime

st.set_page_config(page_title="Pie time! πππ", layout="centered")
st.title("Pie time! πππ")
st.caption("Time and year displayed in π units — because why not?")

now = datetime.now()
decimal_hours = now.hour + now.minute/60 + now.second/3600 + now.microsecond/3600000000
pi_time = decimal_hours / math.pi
pi_year = now.year / math.pi
st.write(f"decimal_hours={decimal_hours}, pi_time={pi_time:.2f}π")


