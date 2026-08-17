# ============================================================
# 🌿 WELLBEING-AI
# AI Mental Wellness & Self-Care Platform
# Main Streamlit Application
# ============================================================

import streamlit as st

from styles import load_css

from components.sidebar import render_sidebar
from components.chat import render_chat
from components.mood import render_mood
from components.journal import render_journal
from components.wellness import render_wellness
from components.insights import render_insights


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="WellBeing-AI",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# LOAD CUSTOM CSS
# ============================================================

load_css()


# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "messages" not in st.session_state:
    st.session_state.messages = []

if "moods" not in st.session_state:
    st.session_state.moods = []

if "journals" not in st.session_state:
    st.session_state.journals = []


# ============================================================
# SIDEBAR
# ============================================================

render_sidebar()

page = st.session_state.page


# ============================================================
# HOME PAGE
# ============================================================

def render_home():

    # --------------------------------------------------------
    # HERO SECTION
    # --------------------------------------------------------

    st.markdown(
        """
        <div class="hero-card">
        <div class="hero-small">🌿 YOUR PERSONAL WELLNESS SPACE</div>
        <div class="hero-title">Welcome to WellBeing-AI 👋</div>
        <div class="hero-description">A calm and supportive space where you can talk, reflect, understand your emotions, and take care of your well-being.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # MOOD CHECK-IN
    # --------------------------------------------------------

    st.markdown(
        """
        <div class="section-heading">
            How are you feeling today? 💚
        </div>
        """,
        unsafe_allow_html=True
    )

    mood_columns = st.columns(5)

    moods = [
        ("😊", "Good", 4),
        ("😄", "Happy", 5),
        ("😐", "Okay", 3),
        ("😟", "Stressed", 2),
        ("😢", "Sad", 1)
    ]

    for column, mood in zip(mood_columns, moods):

        emoji, name, score = mood

        with column:

            if st.button(
                f"{emoji}  {name}",
                key=f"home_mood_{name}",
                use_container_width=True
            ):

                st.session_state.moods.append(
                    {
                        "mood": name,
                        "score": score
                    }
                )

                st.toast(
                    f"Mood saved: {name} 💚"
                )


    # --------------------------------------------------------
    # FEATURE SECTION
    # --------------------------------------------------------

    st.markdown(
        """
        <div class="section-heading">
            What would you like to do?
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    # --------------------------------------------------------
    # AI COMPANION
    # --------------------------------------------------------

    with col1:
        st.markdown(
            """
            <div class="feature-card">
            <div class="feature-icon">💬</div>
            <div class="feature-title">Talk to AI Buddy</div>
            <div class="feature-description">Share your thoughts and have a supportive conversation with WellBeing-AI.</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("Open AI Buddy", key="home_card_chat", use_container_width=True):
            st.session_state.page = "AI Companion"
            st.rerun()

    # --------------------------------------------------------
    # JOURNAL
    # --------------------------------------------------------

    with col2:
        st.markdown(
            """
            <div class="feature-card">
            <div class="feature-icon">📔</div>
            <div class="feature-title">Write a Journal</div>
            <div class="feature-description">Put your thoughts into words and create a private reflection space.</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("Open Journal", key="home_card_journal", use_container_width=True):
            st.session_state.page = "Journal"
            st.rerun()

    # --------------------------------------------------------
    # WELLNESS
    # --------------------------------------------------------

    with col3:
        st.markdown(
            """
            <div class="feature-card">
            <div class="feature-icon">🧘</div>
            <div class="feature-title">Relax & Recharge</div>
            <div class="feature-description">Try breathing, mindfulness and simple wellness activities.</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("Open Wellness", key="home_card_wellness", use_container_width=True):
            st.session_state.page = "Wellness"
            st.rerun()



    # --------------------------------------------------------
    # YOUR JOURNEY
    # --------------------------------------------------------

    st.markdown(
        """
        <div class="section-heading">
            Your Journey 🌱
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)


    # Mood count
    with col1:

        st.metric(
            label="Mood Check-ins",
            value=len(st.session_state.moods)
        )


    # Journal count
    with col2:

        st.metric(
            label="Journal Entries",
            value=len(st.session_state.journals)
        )


    # Conversation count
    with col3:

        conversations = len(
            [
                message
                for message in st.session_state.messages
                if message.get("role") == "user"
            ]
        )

        st.metric(
            label="Conversations",
            value=conversations
        )


    # --------------------------------------------------------
    # REMEMBER CARD
    # --------------------------------------------------------

    st.markdown(
        """
        <div class="remember-card">
        <div class="remember-icon">🌸</div>
        <div>
        <div class="remember-title">Remember</div>
        <div class="remember-text">You don't have to figure everything out at once. One small step is still progress.</div>
        </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# PAGE ROUTING
# ============================================================

if page == "Home":

    render_home()

elif page == "AI Companion":

    render_chat()

elif page == "Mood Check-in":

    render_mood()

elif page == "Journal":

    render_journal()

elif page == "Wellness":

    render_wellness()

elif page == "My Insights":

    render_insights()

else:

    st.session_state.page = "Home"
    st.rerun()
