import streamlit as st
import time


def render_wellness():

    # =====================================================
    # HEADER
    # =====================================================

    st.markdown(
        """
        <div class="chat-header">
        <div class="chat-header-icon">🧘</div>
        <h1>Wellness Space</h1>
        <p>Take a small pause. Choose something that feels comfortable and helpful for you today.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # =====================================================
    # WELLNESS ACTIVITIES
    # =====================================================

    st.markdown(
        '<div class="section-title">Choose an activity 🌱</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    # =====================================================
    # BREATHING
    # =====================================================

    with col1:

        st.markdown(
            """
            <div class="wellness-card">
            <div class="wellness-icon">🌬️</div>
            <h2>Calm Breathing</h2>
            <p>Slow your breathing and give yourself a quiet moment to reset.</p>
            <strong>⏱ 2 minutes</strong>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "🌬️ Start Breathing",
            key="start_breathing",
            use_container_width=True
        ):

            st.session_state.wellness_activity = "breathing"

    # =====================================================
    # MINDFULNESS
    # =====================================================

    with col2:

        st.markdown(
            """
            <div class="wellness-card">
            <div class="wellness-icon">🧘</div>
            <h2>Mindfulness</h2>
            <p>Gently bring your attention back to the present moment.</p>
            <strong>⏱ 5 minutes</strong>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "🧘 Start Mindfulness",
            key="start_mindfulness",
            use_container_width=True
        ):

            st.session_state.wellness_activity = "mindfulness"

    # =====================================================
    # SECOND ROW
    # =====================================================

    st.markdown("<br>", unsafe_allow_html=True)

    col3, col4 = st.columns(2)

    # =====================================================
    # GRATITUDE
    # =====================================================

    with col3:

        st.markdown(
            """
            <div class="wellness-card">
            <div class="wellness-icon">🌸</div>
            <h2>Gratitude</h2>
            <p>Think about one small thing that made today a little better.</p>
            <strong>⏱ 3 minutes</strong>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "🌸 Start Reflection",
            key="start_gratitude",
            use_container_width=True
        ):

            st.session_state.wellness_activity = "gratitude"

    # =====================================================
    # POSITIVE REFLECTION
    # =====================================================

    with col4:

        st.markdown(
            """
            <div class="wellness-card">
            <div class="wellness-icon">✨</div>
            <h2>Positive Reflection</h2>
            <p>Notice something you handled well or something you are proud of.</p>
            <strong>⏱ 5 minutes</strong>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "✨ Start Reflection",
            key="start_positive",
            use_container_width=True
        ):

            st.session_state.wellness_activity = "positive"

    # =====================================================
    # ACTIVE ACTIVITY
    # =====================================================

    activity = st.session_state.get(
        "wellness_activity"
    )

    if activity:

        st.markdown("---")

        if activity == "breathing":

            render_breathing()

        elif activity == "mindfulness":

            render_mindfulness()

        elif activity == "gratitude":

            render_gratitude()

        elif activity == "positive":

            render_positive_reflection()


# =========================================================
# BREATHING EXERCISE
# =========================================================

def render_breathing():

    st.markdown(
        """
        <div class="quote-card">
        <div class="quote-icon">🌬️</div>
        <div>
        <h2>Calm Breathing</h2>
        <p>Find a comfortable position and breathe naturally. Never force your breathing.</p>
        </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### Follow the rhythm")

    st.info(
        """
        🌬️ **Breathe gently**

        **Inhale** — 4 seconds

        **Pause** — 2 seconds

        **Exhale** — 6 seconds

        Repeat comfortably for a few rounds.
        Stop if you feel uncomfortable.
        """
    )

    if st.button(
        "🌱 Complete Exercise",
        key="complete_breathing",
        use_container_width=True
    ):

        st.success(
            "Nice work. You gave yourself a moment to pause. 💚"
        )

        st.session_state.wellness_activity = None


# =========================================================
# MINDFULNESS
# =========================================================

def render_mindfulness():

    st.markdown(
        """
        <div class="quote-card">
        <div class="quote-icon">🧘</div>
        <div>
        <h2>5-Minute Mindfulness</h2>
        <p>Gently notice what is happening around you.</p>
        </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### Try the 5-4-3-2-1 exercise")

    steps = [
        ("5", "things you can see 👀"),
        ("4", "things you can touch ✋"),
        ("3", "things you can hear 👂"),
        ("2", "things you can smell 👃"),
        ("1", "thing you can taste 👅")
    ]

    for number, text in steps:

        st.markdown(
            f"""
            <div class="sense-step">
            <span class="sense-number">{number}</span>
            <span class="sense-text">{text}</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    if st.button(
        "💚 Finish Mindfulness",
        key="complete_mindfulness",
        use_container_width=True
    ):

        st.success(
            "Well done. Take this calm moment with you. 🌿"
        )

        st.session_state.wellness_activity = None


# =========================================================
# GRATITUDE
# =========================================================

def render_gratitude():

    st.markdown(
        """
        <div class="quote-card">
        <div class="quote-icon">🌸</div>
        <div>
        <h2>Gratitude Moment</h2>
        <p>Think of one small thing you appreciate today.</p>
        </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    gratitude = st.text_area(
        "Your gratitude",
        placeholder=(
            "Today I am grateful for..."
        ),
        height=150,
        label_visibility="collapsed"
    )

    if st.button(
        "🌸 Save Reflection",
        key="save_gratitude",
        use_container_width=True
    ):

        if gratitude.strip():

            st.success(
                "Your reflection has been saved for this session. 💚"
            )

        else:

            st.warning(
                "Write a small thought before saving."
            )


# =========================================================
# POSITIVE REFLECTION
# =========================================================

def render_positive_reflection():

    st.markdown(
        """
        <div class="quote-card">
        <div class="quote-icon">✨</div>
        <div>
        <h2>Positive Reflection</h2>
        <p>You don't need a huge achievement. Small wins count too.</p>
        </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    reflection = st.text_area(
        "Your reflection",
        placeholder=(
            "Something I handled well today was..."
        ),
        height=150,
        label_visibility="collapsed"
    )

    if st.button(
        "✨ Save Reflection",
        key="save_positive",
        use_container_width=True
    ):

        if reflection.strip():

            st.success(
                "That's worth celebrating. Keep going. 🌱"
            )

        else:

            st.warning(
                "Write one small positive moment."
            )