import streamlit as st

# ---------------------------------------------------------
# Student Academic Stress Checker (simple, rule-based version)
# No machine learning — just clear if/else logic anyone can follow.
# ---------------------------------------------------------

st.set_page_config(page_title="Student Stress Checker", page_icon="🎓")

st.title("🎓 Student Academic Stress Checker")
st.write("Move the sliders to describe a typical day, then see your result below.")

# --- Inputs ---
study = st.slider("Study hours per day", 0.0, 10.0, 4.0)
sleep = st.slider("Sleep hours per night", 3.0, 10.0, 6.0)
screen = st.slider("Non-academic screen time (hours)", 0.0, 10.0, 5.0)
attendance = st.slider("Attendance percentage", 30, 100, 80)

# --- Rule-based logic ---
# These thresholds are simple rules, not a trained model.
# You can explain each condition in plain English:

def check_stress(study, sleep, screen, attendance):
    if sleep < 5.5 and screen > 5.5:
        return "High", "Low sleep combined with high screen time is a strong stress signal."
    elif study < 3.0 or attendance < 65:
        return "High", "Very low study time or attendance often leads to falling behind."
    elif sleep >= 7.0 and screen <= 3.0:
        return "Low", "Good sleep and controlled screen time usually mean lower stress."
    else:
        return "Medium", "Some habits could improve, but nothing looks urgent yet."

level, explanation = check_stress(study, sleep, screen, attendance)

# --- Output ---
st.subheader(f"Result: {level} stress risk")
st.write(explanation)

# --- Simple suggestions (plain if/else, no fancy formatting needed) ---
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

# --- A simple built-in chart (no extra libraries needed) ---
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
