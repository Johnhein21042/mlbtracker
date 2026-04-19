import streamlit as st
import pandas as pd

st.set_page_config(page_title="MLB Bet Tracker", layout="centered")

st.title("🏟️ MLB Bet Tracker")
st.caption("Tracking 6 teams - updated live")

data = {
    "Baltimore": {"line": 84.5, "type": "over", "current": 12},
    "Detroit": {"line": 85.5, "type": "over", "current": 11},
    "Milwaukee": {"line": 84.5, "type": "over", "current": 10},
    "Kansas City": {"line": 81.5, "type": "over", "current": 9},
    "Minnesota": {"line": 74.5, "type": "under", "current": 13},
    "San Diego": {"line": 85.5, "type": "under", "current": 12}
}

st.subheader("Season Progress")
for team, info in data.items():
    current = info line = info if info["type"] == "over":
        needed = line - current
        status = "✅ On pace" if current >= line * 0.6 else "❌ Behind pace"
    else:
        needed = current - line
        status = "✅ On pace" if current <= line * 0.6 else "❌ Behind pace"
    
    st.write(f"**{team}**: {current} wins • needs {needed} more • {status}")

st.caption("Numbers are placeholders - we'll connect real data next")
