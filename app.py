import streamlit as st

# ---------------------------------------------------------
# Student Academic Stress Checker (simple, rule-based version)
# No machine learning — just clear if/else logic anyone can follow.
# ---------------------------------------------------------

st.set_page_config(page_title="Student Stress Checker", page_icon="🎓", layout="centered")

COLORS = {
    "High": "#B5473B",
    "Medium": "#C98A2C",
    "Low": "#2F7A67",
}

# --- Styling ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=IBM+Plex+Sans:wght@400;500;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'IBM Plex Sans', sans-serif;
    }
    h1, h2, h3 {
        font-family: 'Fraunces', serif;
        font-weight: 600;
    }
    .block-container {
        padding-top: 2.5rem;
        max-width: 760px;
    }
    .subtitle {
        color: #5B6B63;
        font-size: 1.02rem;
        margin-top: -0.6rem;
        margin-bottom: 1.8rem;
    }
    .result-band {
        border-radius: 6px;
        padding: 1.1rem 1.4rem;
        margin-bottom: 1.6rem;
        border-left: 5px solid;
    }
    .result-band .risk-level {
        font-family: 'Fraunces', serif;
        font-size: 1.4rem;
        font-weight: 600;
        margin-bottom: 0.2rem;
    }
    .result-band .risk-explanation {
        color: #3A4A42;
        font-size: 0.98rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Rule-based logic ---
def check_stress(study, sleep, screen, attendance):
    if sleep < 5.5 and screen > 5.5:
        return "High", "Low sleep combined with high screen time is a strong stress signal."
    elif study < 3.0 or attendance < 65:
        return "High", "Very low study time or attendance often leads to falling behind."
    elif sleep >= 7.0 and screen <= 3.0:
        return "Low", "Good sleep and controlled screen time usually mean lower stress."
    else:
        return "Medium", "Some habits could improve, but nothing looks urgent yet."

# --- Header ---
st.title("🎓 Student Academic Stress Checker")
st.markdown('<p class="subtitle">Move the sliders to describe a typical day, then see your result below.</p>', unsafe_allow_html=True)

# --- Sidebar inputs ---
with st.sidebar:
    st.header("Describe your day")
    study = st.slider("Study hours per day", 0.0, 10.0, 4.0)
    sleep = st.slider("Sleep hours per night", 3.0, 10.0, 6.0)
    screen = st.slider("Non-academic screen time (hours)", 0.0, 10.0, 5.0)
    attendance = st.slider("Attendance percentage", 30, 100, 80)
    st.divider()
    st.caption(
        "This is a rule-based tool for a school project, "
        "not a medical or psychological assessment."
    )

level, explanation = check_stress(study, sleep, screen, attendance)
accent = COLORS[level]

# --- Result band ---
st.markdown(
    f"""
    <div class="result-band" style="background:{accent}15; border-left-color:{accent};">
      <div class="risk-level" style="color:{accent};">{level} stress risk</div>
      <div class="risk-explanation">{explanation}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- Suggestions (unchanged for now) ---
st.subheader("Suggestions")

if sleep < 7.0:
    st.write(f"- Try to sleep {7.0 - sleep:.1f} more hour(s) per night.")

if screen > 2.5:
    st.write(f"- Try to cut screen time by {screen - 2.5:.1f} hour(s) per day.")

if attendance < 75:
    st.write(f"- Attendance is {75 - attendance}% below a safe margin — prioritize your next few classes.")

if study < 4.0:
    st.write(f"- Try to add {4.0 - study:.1f} more study hour(s) per day, in short focused sessions.")

if sleep >= 7.0 and screen <= 2.5 and attendance >= 75 and study >= 4.0:
    st.write("- Your habits look balanced. Keep it up!")

# --- Chart (unchanged for now) ---
st.subheader("Your day vs. a healthy target")
chart_data = {
    "You": [study, sleep, max(0, 10 - screen), attendance / 10],
    "Target": [4.0, 7.5, 7.5, 9.0],
}
st.bar_chart(chart_data)

st.caption(
    "Note: this is a simple rule-based tool for a school project, "
    "not a medical or psychological assessment."
)
