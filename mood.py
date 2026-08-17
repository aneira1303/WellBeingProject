import streamlit as st
from datetime import datetime


def render_mood():

    # =====================================================
    # HEADER
    # =====================================================

    st.markdown(
        """
        <div class="chat-header">
        <div class="chat-header-icon">😊</div>
        <h1>Mood Check-in</h1>
        <p>Take a moment to check in with yourself. There are no right or wrong answers.</p>
        </div>
        """,
        unsafe_allow_html=True
    )


    # =====================================================
    # MOOD SELECTION
    # =====================================================

    st.markdown(
        '<div class="section-title">How are you feeling right now?</div>',
        unsafe_allow_html=True
    )

    moods = [
        ("😄", "Happy", 5),
        ("😊", "Good", 4),
        ("😐", "Okay", 3),
        ("😟", "Stressed", 2),
        ("😢", "Sad", 1)
    ]

    if "mood_choice" not in st.session_state:
        st.session_state.mood_choice = None

    columns = st.columns(5)


    for column, (emoji, name, score) in zip(
        columns,
        moods
    ):

        with column:

            is_selected = (
                st.session_state.mood_choice is not None
                and st.session_state.mood_choice["mood"] == name
            )

            card_class = (
                "mood-card mood-card-selected"
                if is_selected
                else "mood-card"
            )

            st.markdown(
                f"""
                <div class="{card_class}">
                <div class="mood-emoji">{emoji}</div>
                <div class="mood-title">{name}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

            button_label = (
                f"✓ {name}"
                if is_selected
                else f"Choose {name}"
            )

            if st.button(
                button_label,
                key=f"mood_select_{name}",
                use_container_width=True
            ):

                st.session_state.mood_choice = {
                    "mood": name,
                    "score": score
                }

                st.rerun()


    # =====================================================
    # CURRENT SELECTION
    # =====================================================

    if st.session_state.mood_choice:

        st.success(
            f"Selected mood: **{st.session_state.mood_choice['mood']}** 💚 "
            "— add a note below and save, or save now."
        )


    # =====================================================
    # OPTIONAL NOTE
    # =====================================================

    st.markdown(
        '<div class="section-title">Want to say a little more?</div>',
        unsafe_allow_html=True
    )

    note = st.text_area(
        "Mood note",
        placeholder=(
            "What is making you feel this way?"
        ),
        height=120,
        label_visibility="collapsed"
    )

    if st.button(
        "💚 Save Mood & Note",
        key="save_mood_note",
        use_container_width=True
    ):

        if not st.session_state.mood_choice:

            st.warning(
                "Please select a mood first."
            )

        else:

            st.session_state.moods.append(
                {
                    "mood": st.session_state.mood_choice["mood"],
                    "score": st.session_state.mood_choice["score"],
                    "note": note,
                    "date": datetime.now().strftime(
                        "%d %b %Y, %I:%M %p"
                    )
                }
            )

            st.session_state.mood_choice = None

            st.success(
                "Your check-in has been saved 🌱"
            )

            st.rerun()


    # =====================================================
    # CURRENT MOOD
    # =====================================================

    st.markdown("---")

    st.markdown(
        '<div class="section-title">Your latest check-in</div>',
        unsafe_allow_html=True
    )


    if st.session_state.moods:

        latest = st.session_state.moods[-1]

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Current Mood",
                latest["mood"]
            )

        with col2:

            score = latest.get(
                "score",
                3
            )

            st.metric(
                "Mood Score",
                f"{score}/5"
            )

        st.progress(
            score / 5
        )

        if latest.get("note"):

            st.markdown(
                f"""
                <div class="quote-card">
                <div class="quote-icon">💭</div>
                <div>
                <strong>Your note</strong>
                <p>{latest["note"]}</p>
                </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    else:

        st.info(
            "You haven't recorded a mood yet. "
            "Choose one above to begin."
        )


    # =====================================================
    # MOOD HISTORY
    # =====================================================

    if len(st.session_state.moods) > 1:

        st.markdown("---")

        st.markdown(
            '<div class="section-title">Mood History</div>',
            unsafe_allow_html=True
        )

        for entry in reversed(
            st.session_state.moods[-5:]
        ):

            st.write(
                f"🌿 **{entry['mood']}** — "
                f"{entry.get('date', '')}"
            )