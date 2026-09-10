import streamlit as st

# ---------------------------------------------------------
# Student Academic Stress Checker (simple, rule-based version)
# No machine learning — just clear if/else logic anyone can follow.
# ---------------------------------------------------------

st.set_page_config(page_title="Student Stress Checker", page_icon="🎓", layout="centered")

TARGET_STUDY = 4.0
TARGET_SLEEP = 7.5
TARGET_SCREEN = 2.5
TARGET_ATTENDANCE = 90

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
    .bar-row {
        display: flex;
        align-items: center;
        gap: 14px;
        margin-bottom: 16px;
    }
    .bar-label {
        width: 118px;
        font-size: 0.88rem;
        color: #5B6B63;
        flex-shrink: 0;
    }
    .bar-track {
        position: relative;
        flex: 1;
        height: 10px;
        background: #DCE5E0;
        border-radius: 6px;
    }
    .bar-fill {
        position: absolute;
        left: 0;
        top: 0;
        height: 100%;
        border-radius: 6px;
    }
    .bar-target {
        position: absolute;
        top: -4px;
        width: 2px;
        height: 18px;
        background: #1F2A24;
        opacity: 0.45;
    }
    .bar-value {
        width: 56px;
        text-align: right;
        font-size: 0.88rem;
        color: #1F2A24;
        font-variant-numeric: tabular-nums;
        flex-shrink: 0;
    }
    .bar-legend {
        font-size: 0.82rem;
        color: #5B6B63;
        margin-top: -4px;
        margin-bottom: 1.6rem;
    }
    .tip-card {
        background: #FFFFFF;
        border-left: 4px solid;
        border-radius: 4px;
        padding: 0.65rem 0.9rem;
        margin-bottom: 0.55rem;
        font-size: 0.95rem;
        color: #1F2A24;
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


def build_suggestions(study, sleep, screen, attendance):
    tips = []
    if sleep < 7.0:
        tips.append(f"Try to sleep {7.0 - sleep:.1f} more hour(s) per night.")
    if screen > 2.5:
        tips.append(f"Try to cut screen time by {screen - 2.5:.1f} hour(s) per day.")
    if attendance < 75:
        tips.append(f"Attendance is {75 - attendance}% below a safe margin — prioritize your next few classes.")
    if study < 4.0:
        tips.append(f"Try to add {4.0 - study:.1f} more study hour(s) per day, in short focused sessions.")
    if not tips:
        tips.append("Your habits look balanced. Keep it up!")
    return tips


def bar_color(value, target):
    ratio = value / target if target else 1
    if ratio >= 1:
        return "#2F7A67"
    elif ratio >= 0.7:
        return "#C98A2C"
    return "#B5473B"


def bar_row(label, value, target, max_scale, unit=""):
    value_pct = max(0, min(100, (value / max_scale) * 100))
    target_pct = max(0, min(100, (target / max_scale) * 100))
    color = bar_color(value, target)
    return (
        '<div class="bar-row">'
        f'<div class="bar-label">{label}</div>'
        '<div class="bar-track">'
        f'<div class="bar-target" style="left:{target_pct:.1f}%;"></div>'
        f'<div class="bar-fill" style="width:{value_pct:.1f}%; background:{color};"></div>'
        '</div>'
        f'<div class="bar-value">{value:.0f}{unit}</div>'
        '</div>'
    )


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

# --- Quick stats ---
c1, c2, c3, c4 = st.columns(4)
c1.metric("Study", f"{study:.1f}h", f"{study - TARGET_STUDY:+.1f} vs target")
c2.metric("Sleep", f"{sleep:.1f}h", f"{sleep - TARGET_SLEEP:+.1f} vs target")
c3.metric("Screen time", f"{screen:.1f}h", f"{screen - TARGET_SCREEN:+.1f} vs target", delta_color="inverse")
c4.metric("Attendance", f"{attendance}%", f"{attendance - TARGET_ATTENDANCE:+d} vs target")

# --- Comparison bars ---
st.subheader("Your day, at a glance")

bars_html = "".join([
    bar_row("Study", study, TARGET_STUDY, 10, "h"),
    bar_row("Sleep", sleep, TARGET_SLEEP, 10, "h"),
    bar_row("Screen control", max(0, 10 - screen), 10 - TARGET_SCREEN, 10, "h"),
    bar_row("Attendance", attendance, TARGET_ATTENDANCE, 100, "%"),
])
st.markdown(bars_html, unsafe_allow_html=True)
st.markdown(
    '<p class="bar-legend">The thin vertical mark on each bar shows the healthy target. '
    '"Screen control" is 10 minus your screen time, so a longer bar is better here too.</p>',
    unsafe_allow_html=True,
)

# --- Suggestions ---
st.subheader("Suggestions")
tips_html = "".join(
    f'<div class="tip-card" style="border-left-color:{accent};">{tip}</div>'
    for tip in build_suggestions(study, sleep, screen, attendance)
)
st.markdown(tips_html, unsafe_allow_html=True)

with st.expander("How is this calculated?"):
    st.markdown(
        """
        This tool uses simple if/else rules, not machine learning or AI:

        - **High risk** — low sleep *and* high screen time, OR very low study time/attendance
        - **Low risk** — good sleep *and* controlled screen time
        - **Medium risk** — everything in between

        Targets used above: 7.5h sleep, 2.5h non-academic screen time, 4h focused study, 90%+ attendance.
        """
    )
