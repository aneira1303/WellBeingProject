import streamlit as st


def render_sidebar():

    with st.sidebar:

        # ====================================================
        # LOGO
        # ====================================================

        st.markdown(
            """
            <div class="sidebar-brand">
            <div class="sidebar-logo">🌿</div>
            <div class="sidebar-title">WellBeing-AI</div>
            <div class="sidebar-subtitle">Your space to breathe & grow</div>
            </div>
            """,
            unsafe_allow_html=True
        )


        # ====================================================
        # NAVIGATION
        # ====================================================

        st.markdown("### Navigation")

        pages = [
            ("🏠", "Home"),
            ("💬", "AI Companion"),
            ("😊", "Mood Check-in"),
            ("📔", "Journal"),
            ("🧘", "Wellness"),
            ("📊", "My Insights"),
        ]


        for icon, name in pages:

            if st.button(
                f"{icon}  {name}",
                key=f"sidebar_{name}",
                use_container_width=True
            ):

                st.session_state.page = name
                st.rerun()


        # ====================================================
        # SUPPORT
        # ====================================================

        st.divider()

        st.info(
            "💚 Take a moment for yourself.\n\n"
            "You don't have to do everything at once."
        )


        # ====================================================
        # FOOTER
        # ====================================================

        st.caption(
            "WellBeing-AI 🌱"
        )


    return st.session_state.get(
        "page",
        "Home"
    )
