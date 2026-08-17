import streamlit as st
from collections import Counter


def render_insights():

    # =====================================================
    # HEADER
    # =====================================================

    st.markdown(
        """
        <div class="chat-header">
        <div class="chat-header-icon">📊</div>
        <h1>My Insights</h1>
        <p>A simple view of your WellBeing-AI journey. Notice patterns, celebrate progress and keep going.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # =====================================================
    # BASIC STATISTICS
    # =====================================================

    mood_count = len(
        st.session_state.get("moods", [])
    )

    journal_count = len(
        st.session_state.get("journals", [])
    )

    messages = st.session_state.get(
        "messages",
        []
    )

    user_message_count = len(
        [
            message
            for message in messages
            if message.get("role") == "user"
        ]
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            f"""
            <div class="stat-card">
            <div class="stat-number">{mood_count}</div>
            <div class="stat-label">😊 Mood Check-ins</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            f"""
            <div class="stat-card">
            <div class="stat-number">{journal_count}</div>
            <div class="stat-label">📔 Journal Entries</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            f"""
            <div class="stat-card">
            <div class="stat-number">{user_message_count}</div>
            <div class="stat-label">💬 AI Conversations</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # =====================================================
    # MOOD OVERVIEW
    # =====================================================

    st.markdown(
        '<div class="section-title">😊 Mood Overview</div>',
        unsafe_allow_html=True
    )

    moods = st.session_state.get(
        "moods",
        []
    )

    if not moods:

        st.info(
            "Complete a few mood check-ins to see your mood insights."
        )

    else:

        mood_names = [
            mood.get("mood", "Unknown")
            for mood in moods
        ]

        mood_counts = Counter(
            mood_names
        )

        col1, col2 = st.columns(2)

        # -------------------------------------------------
        # MOOD FREQUENCY
        # -------------------------------------------------

        with col1:

            st.markdown(
                "### Your mood pattern"
            )

            for mood, count in mood_counts.items():

                st.write(
                    f"{mood}: **{count} check-in(s)**"
                )

        # -------------------------------------------------
        # MOOD SCORE
        # -------------------------------------------------

        with col2:

            scores = [
                mood.get("score", 3)
                for mood in moods
            ]

            if scores:

                average_score = (
                    sum(scores) / len(scores)
                )

                st.metric(
                    "Average Mood Score",
                    f"{average_score:.1f}/5"
                )

                st.progress(
                    min(
                        average_score / 5,
                        1.0
                    )
                )

    # =====================================================
    # MOOD CHART
    # =====================================================

    if moods:

        st.markdown(
            "### 📈 Mood Trend"
        )

        chart_data = {
            "Mood Score": [
                mood.get("score", 3)
                for mood in moods
            ]
        }

        st.line_chart(
            chart_data,
            height=300
        )

    # =====================================================
    # JOURNAL INSIGHTS
    # =====================================================

    st.markdown(
        '<div class="section-title">📔 Journal Activity</div>',
        unsafe_allow_html=True
    )

    journals = st.session_state.get(
        "journals",
        []
    )

    if not journals:

        st.info(
            "Your journal activity will appear here "
            "after you create your first entry."
        )

    else:

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Total Entries",
                len(journals)
            )

        with col2:

            latest = journals[-1]

            st.metric(
                "Latest Mood",
                latest.get(
                    "mood",
                    "Not specified"
                )
            )

    # =====================================================
    # AI COMPANION ACTIVITY
    # =====================================================

    st.markdown(
        '<div class="section-title">💬 AI Companion Activity</div>',
        unsafe_allow_html=True
    )

    if user_message_count == 0:

        st.info(
            "Start a conversation with WellBeing-AI "
            "to see your activity here."
        )

    else:

        st.success(
            f"You have shared {user_message_count} "
            f"thought(s) with WellBeing-AI during this session. 🌿"
        )

    # =====================================================
    # WELLNESS MESSAGE
    # =====================================================

    st.markdown(
        """
        <div class="quote-card">
        <div class="quote-icon">🌱</div>
        <div>
        <h3>Your journey matters</h3>
        <p>Wellness isn't about being positive all the time. It's about noticing how you're doing and giving yourself space to care for yourself.</p>
        </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # =====================================================
    # RESET SESSION DATA
    # =====================================================

    st.markdown("---")

    with st.expander(
        "⚙️ Session Data"
    ):

        st.write(
            "The current UI stores your demo data "
            "in Streamlit session memory."
        )

        if st.button(
            "🗑️ Clear Session Data",
            key="clear_session_data"
        ):

            st.session_state.moods = []
            st.session_state.journals = []
            st.session_state.messages = []

            st.success(
                "Session data cleared."
            )

            st.rerun()