import streamlit as st
from datetime import datetime


def render_journal():

    # =====================================================
    # HEADER
    # =====================================================

    st.markdown(
        """
        <div class="chat-header">
        <div class="chat-header-icon">📔</div>
        <h1>My Journal</h1>
        <p>Your private space to write, reflect and express yourself.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # =====================================================
    # NEW JOURNAL ENTRY
    # =====================================================

    st.markdown(
        '<div class="section-title">How are you feeling today?</div>',
        unsafe_allow_html=True
    )

    journal_title = st.text_input(
        "Title",
        placeholder="Give your entry a title...",
        label_visibility="collapsed"
    )

    journal_text = st.text_area(
        "Journal",
        placeholder=(
            "Write whatever is on your mind...\n\n"
            "You can write about your feelings, "
            "your day, your goals, challenges, "
            "or something you are grateful for."
        ),
        height=280,
        label_visibility="collapsed"
    )

    # =====================================================
    # MOOD FOR JOURNAL
    # =====================================================

    st.markdown(
        "### 😊 How does this entry feel?"
    )

    journal_mood = st.selectbox(
        "Mood",
        [
            "😊 Happy",
            "🙂 Good",
            "😐 Okay",
            "😟 Stressed",
            "😢 Sad",
            "😰 Anxious"
        ],
        label_visibility="collapsed"
    )

    # =====================================================
    # SAVE
    # =====================================================

    if st.button(
        "💚 Save Journal Entry",
        key="save_journal",
        use_container_width=True
    ):

        if not journal_text.strip():

            st.warning(
                "Please write something before saving your entry."
            )

        else:

            entry = {
                "title": (
                    journal_title.strip()
                    if journal_title.strip()
                    else "My Journal Entry"
                ),
                "text": journal_text.strip(),
                "mood": journal_mood,
                "date": datetime.now().strftime(
                    "%d %b %Y, %I:%M %p"
                )
            }

            st.session_state.journals.append(entry)

            st.success(
                "Your journal entry has been saved 🌱"
            )

            st.balloons()

    # =====================================================
    # JOURNAL STATISTICS
    # =====================================================

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "📔 Entries",
            len(st.session_state.journals)
        )

    with col2:

        if st.session_state.journals:
            latest_mood = st.session_state.journals[-1]["mood"]
        else:
            latest_mood = "—"

        st.metric(
            "😊 Latest Mood",
            latest_mood
        )

    with col3:

        if st.session_state.journals:
            latest_date = st.session_state.journals[-1]["date"]
        else:
            latest_date = "—"

        st.metric(
            "🕒 Latest Entry",
            latest_date
        )

    # =====================================================
    # PREVIOUS ENTRIES
    # =====================================================

    st.markdown(
        '<div class="section-title">📚 Previous Entries</div>',
        unsafe_allow_html=True
    )

    if not st.session_state.journals:

        st.info(
            "You don't have any journal entries yet. "
            "Your first entry will appear here."
        )

    else:

        for index, entry in enumerate(
            reversed(st.session_state.journals)
        ):

            title = entry.get(
                "title",
                "My Journal Entry"
            )

            date = entry.get(
                "date",
                ""
            )

            mood = entry.get(
                "mood",
                "😊 Good"
            )

            text = entry.get(
                "text",
                ""
            )

            with st.expander(
                f"📔 {title}  •  {date}"
            ):

                st.markdown(
                    f"**Mood:** {mood}"
                )

                st.markdown(
                    f"**Entry:**"
                )

                st.write(text)

                st.markdown("")

                if st.button(
                    "🗑️ Delete",
                    key=f"delete_journal_{index}"
                ):

                    actual_index = (
                        len(st.session_state.journals)
                        - 1
                        - index
                    )

                    st.session_state.journals.pop(
                        actual_index
                    )

                    st.rerun()
