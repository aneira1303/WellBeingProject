import html
import textwrap
import streamlit as st
from groq import Groq


# =========================================================
# GROQ CLIENT
# =========================================================

def get_groq_client():

    try:
        api_key = st.secrets["GROQ_API_KEY"]

        return Groq(
            api_key=api_key
        )

    except Exception:
        return None


# =========================================================
# SYSTEM PROMPT
# =========================================================

SYSTEM_PROMPT = """
You are WellBeing-AI, an AI mental wellness companion.

Your purpose is to provide a calm, empathetic and supportive
space where users can talk about their thoughts and emotions.

Guidelines:

1. Listen carefully to the user's concerns.
2. Respond with empathy and kindness.
3. Help users understand and reflect on their emotions.
4. Provide practical and simple wellness suggestions.
5. You may suggest:
   - breathing exercises
   - mindfulness
   - journaling
   - relaxation
   - healthy routines
   - stress-management techniques
6. Do not diagnose mental health disorders.
7. Do not claim to be a doctor, psychologist or therapist.
8. Do not prescribe medication.
9. Avoid judgmental or dismissive responses.
10. Keep responses conversational and supportive.
11. Do not overwhelm the user with too many suggestions.
12. Ask gentle follow-up questions when appropriate.
13. If the user appears to be in immediate danger or describes
    serious self-harm or suicide intent, encourage them to seek
    immediate professional or emergency support and contact a
    trusted person nearby.

Your name is WellBeing-AI.

Respond naturally and empathetically.
"""


# =========================================================
# SEND MESSAGE TO GROQ
# =========================================================

def send_message(message):

    client = get_groq_client()

    if client is None:

        return {
            "error": (
                "GROQ_API_KEY is not configured in "
                "Streamlit Secrets."
            )
        }

    try:

        # -------------------------------------------------
        # SYSTEM MESSAGE
        # -------------------------------------------------

        groq_messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

        # -------------------------------------------------
        # CONVERSATION MEMORY
        # -------------------------------------------------

        history = st.session_state.messages[:-1]

        # Keep the most recent messages
        history = history[-12:]

        for chat_message in history:

            role = chat_message.get("role")
            content = chat_message.get("content", "")

            if role in ["user", "assistant"]:

                groq_messages.append(
                    {
                        "role": role,
                        "content": content
                    }
                )

        # -------------------------------------------------
        # CURRENT USER MESSAGE
        # -------------------------------------------------

        groq_messages.append(
            {
                "role": "user",
                "content": message
            }
        )

        # -------------------------------------------------
        # GROQ API CALL
        # -------------------------------------------------

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=groq_messages,
            temperature=0.7,
            max_tokens=700
        )

        ai_response = response.choices[0].message.content

        return {
            "response": ai_response,
            "emotion": "neutral",
            "risk_level": "low",
            "sources": []
        }

    except Exception as error:

        return {
            "error": str(error)
        }


# =========================================================
# CHAT UI
# =========================================================

def render_chat():

    # -----------------------------------------------------
    # SESSION STATE
    # -----------------------------------------------------

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # -----------------------------------------------------
    # HEADER
    # -----------------------------------------------------

    st.markdown(
        textwrap.dedent("""\
        <div class="chat-header">
        <div class="chat-header-icon">🌿</div>
        <h1>AI Companion</h1>
        <p>A safe and supportive space to talk, reflect and feel heard.</p>
        </div>
        """),
        unsafe_allow_html=True
    )

    # -----------------------------------------------------
    # SHOW LAST ERROR (persists across reruns)
    # -----------------------------------------------------

    if st.session_state.get("last_error"):
        with st.expander("⚠️ Last connection error (click to view)"):
            st.code(st.session_state.last_error)

    # -----------------------------------------------------
    # INITIAL MESSAGE
    # -----------------------------------------------------

    if not st.session_state.messages:
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": (
                    "Hi! 👋 I'm WellBeing-AI. "
                    "I'm here to listen. "
                    "What's on your mind today?"
                )
            }
        )

    # -----------------------------------------------------
    # DISPLAY CHAT HISTORY
    # -----------------------------------------------------

    for message in st.session_state.messages:

        content = message.get("content", "")

        # Escape HTML so user/AI text doesn't break your custom UI.
        safe_content = html.escape(content)
        safe_content = safe_content.replace("\n", "<br>")

        # ---------------------------------------------
        # USER MESSAGE
        # ---------------------------------------------

        if message["role"] == "user":
            st.markdown(
                f"""<div class="user-message">
<div class="message-name">You</div>
<div>{safe_content}</div>
</div>""",
                unsafe_allow_html=True
            )

        # ---------------------------------------------
        # AI MESSAGE
        # ---------------------------------------------

        else:
            st.markdown(
                f"""<div class="ai-message">
<div class="message-name">🌿 WellBeing-AI</div>
<div>{safe_content}</div>
</div>""",
                unsafe_allow_html=True
            )

    # -----------------------------------------------------
    # QUICK CHECK-IN
    # -----------------------------------------------------

    st.markdown("### Quick check-in 💚")

    col1, col2, col3, col4 = st.columns(4)

    selected_message = None

    # -----------------------------------------------------
    # STRESSED
    # -----------------------------------------------------

    with col1:
        if st.button(
            "😟 I'm stressed",
            key="quick_stressed",
            use_container_width=True
        ):
            selected_message = "I'm feeling stressed."

    # -----------------------------------------------------
    # SAD
    # -----------------------------------------------------

    with col2:
        if st.button(
            "😢 I'm feeling sad",
            key="quick_sad",
            use_container_width=True
        ):
            selected_message = "I'm feeling sad."

    # -----------------------------------------------------
    # ANXIOUS
    # -----------------------------------------------------

    with col3:
        if st.button(
            "😰 I'm anxious",
            key="quick_anxious",
            use_container_width=True
        ):
            selected_message = "I'm feeling anxious."

    # -----------------------------------------------------
    # GOOD
    # -----------------------------------------------------

    with col4:
        if st.button(
            "😊 I'm doing well",
            key="quick_good",
            use_container_width=True
        ):
            selected_message = "I'm feeling good today."

    # -----------------------------------------------------
    # CHAT INPUT
    # -----------------------------------------------------

    user_message = st.chat_input("Tell me what's on your mind...")

    # Quick check-in overrides chat input

    if selected_message:
        user_message = selected_message

    # -----------------------------------------------------
    # PROCESS MESSAGE
    # -----------------------------------------------------

    if user_message:

        # -------------------------------------------------
        # SAVE USER MESSAGE
        # -------------------------------------------------

        st.session_state.messages.append(
            {
                "role": "user",
                "content": user_message
            }
        )

        # -------------------------------------------------
        # CALL GROQ
        # -------------------------------------------------

        with st.spinner("WellBeing-AI is thinking... 🌿"):
            result = send_message(user_message)

        # -------------------------------------------------
        # PROCESS ERROR
        # -------------------------------------------------

        if "error" in result:

            # Print to terminal so you can always see the real cause
            print("GROQ ERROR:", result["error"])

            # Store in session_state so it survives the rerun
            # and can be displayed persistently in the UI
            st.session_state.last_error = result["error"]

            ai_response = (
                "I'm unable to connect to the AI "
                "service right now. Please try again "
                "in a moment."
            )

        # -------------------------------------------------
        # PROCESS SUCCESS
        # -------------------------------------------------

        else:

            ai_response = result.get(
                "response",
                (
                    "I'm here with you. "
                    "Tell me more about what "
                    "you're experiencing."
                )
            )

            # -------------------------------------------------
            # STORE METADATA
            # -------------------------------------------------

            st.session_state.last_emotion = result.get("emotion", "neutral")
            st.session_state.last_risk = result.get("risk_level", "low")
            st.session_state.last_sources = result.get("sources", [])

        # -------------------------------------------------
        # SAVE AI RESPONSE
        # -------------------------------------------------

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": ai_response
            }
        )

        # -------------------------------------------------
        # REFRESH UI
        # -------------------------------------------------

        st.rerun()