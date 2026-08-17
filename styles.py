# ============================================================
# 🌿 WELLBEING-AI
# Global CSS Styling — "Lavender Bloom" design system
#
# Design tokens:
#   Color   → lavender-forward gradient world, deep plum-lavender
#             ink, soft blush pink for action/energy, a lighter
#             lavender-violet for gentle emphasis.
#   Type    → Fraunces (warm, soft-curved serif) for anything
#             that should feel human and unhurried; Plus Jakarta
#             Sans (rounded, friendly) for everything you read
#             quickly — buttons, labels, body copy.
#   Motion  → one signature move: the hero card breathes. A slow
#             8s glow pulse (roughly a 4s-in / 4s-out breath)
#             around the welcome card, echoing the sidebar's own
#             "space to breathe" line. Disabled for users who
#             prefer reduced motion.
# ============================================================

import streamlit as st


def load_css():

    st.markdown(
        """
        <style>

        @import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,400;0,500;0,600;0,700;1,500&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');


        /* ====================================================
           DESIGN TOKENS
        ==================================================== */

        :root {

            --bg-grad-1: #ece3fb;
            --bg-grad-2: #e2d4f7;

            --surface: #ffffff;
            --surface-soft: #f5eefb;

            --ink-900: #352a4f;
            --ink-700: #574a70;
            --ink-500: #8d81a5;

            --accent-violet: #a48ee8;
            --accent-violet-deep: #7c5cf0;
            --accent-coral: #f78fc0;
            --accent-coral-deep: #e85caa;

            --border-soft: #e8ddf7;

            --shadow-violet: rgba(124, 92, 240, 0.14);
            --shadow-coral: rgba(232, 92, 170, 0.16);

            --font-display: 'Fraunces', Georgia, serif;
            --font-body: 'Plus Jakarta Sans', -apple-system, sans-serif;

        }


        /* ====================================================
           GLOBAL APP
        ==================================================== */

        .stApp {
            background:
                radial-gradient(1200px 600px at 10% -5%, var(--bg-grad-1) 0%, transparent 60%),
                radial-gradient(1200px 700px at 100% 10%, var(--bg-grad-2) 0%, transparent 55%),
                #f7f2fd;
            color: var(--ink-700);
            font-family: var(--font-body);
        }


        /* ====================================================
           MAIN CONTENT
        ==================================================== */

        .main .block-container {
            max-width: 1360px;
            padding-top: 2rem;
            padding-bottom: 4rem;
            padding-left: 2.5rem;
            padding-right: 2.5rem;
        }


        /* ====================================================
           TYPOGRAPHY
        ==================================================== */

        h1, h2, h3 {
            font-family: var(--font-display) !important;
            color: var(--ink-900) !important;
            font-weight: 600 !important;
        }

        p, span, div, label {
            font-family: var(--font-body);
        }


        /* ====================================================
           SIDEBAR
        ==================================================== */

        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #ffffff 0%, var(--surface-soft) 100%);
            border-right: 1px solid var(--border-soft);
        }

        [data-testid="stSidebar"] .block-container {
            padding-top: 1.75rem;
            padding-left: 1.1rem;
            padding-right: 1.1rem;
        }


        /* ====================================================
           SIDEBAR BRAND
        ==================================================== */

        .sidebar-brand {
            text-align: center;
            padding: 6px 10px 26px 10px;
        }

        .sidebar-logo {
            font-size: 40px;
            line-height: 1;
            margin-bottom: 10px;
            filter: drop-shadow(0 4px 10px var(--shadow-violet));
        }

        .sidebar-title {
            font-family: var(--font-display);
            font-size: 23px;
            font-weight: 600;
            color: var(--ink-900);
        }

        .sidebar-subtitle {
            font-size: 12.5px;
            color: var(--ink-500);
            margin-top: 5px;
            font-style: italic;
            font-family: var(--font-display);
        }


        /* ====================================================
           HERO CARD  (signature: the breathing halo)
        ==================================================== */

        .hero-card {
            position: relative;
            width: 100%;
            box-sizing: border-box;

            background: linear-gradient(135deg, #ffffff 0%, var(--surface-soft) 100%);

            border: 1px solid var(--border-soft);
            border-radius: 28px;

            padding: 46px 50px;
            margin-bottom: 30px;
            overflow: hidden;

            box-shadow: 0 10px 40px var(--shadow-violet);
            animation: breathe 8s ease-in-out infinite;
        }

        .hero-card::before {
            content: "";
            position: absolute;
            top: -40%;
            right: -15%;
            width: 420px;
            height: 420px;
            border-radius: 50%;
            background: radial-gradient(circle, var(--shadow-coral) 0%, transparent 70%);
            pointer-events: none;
        }

        @keyframes breathe {
            0%, 100% {
                box-shadow: 0 10px 40px var(--shadow-violet);
                transform: scale(1);
            }
            50% {
                box-shadow: 0 14px 54px var(--shadow-violet), 0 0 0 10px rgba(139, 127, 217, 0.05);
                transform: scale(1.004);
            }
        }

        @media (prefers-reduced-motion: reduce) {
            .hero-card {
                animation: none;
            }
        }

        .hero-small {
            position: relative;
            display: inline-block;
            font-family: var(--font-body);
            font-size: 12.5px;
            font-weight: 700;
            letter-spacing: 1.6px;
            color: var(--accent-violet-deep);
            background: rgba(139, 127, 217, 0.1);
            padding: 6px 14px;
            border-radius: 999px;
            margin-bottom: 18px;
        }

        .hero-title {
            position: relative;
            font-family: var(--font-display);
            font-size: 40px;
            line-height: 1.2;
            font-weight: 600;
            color: var(--ink-900);
            margin-bottom: 14px;
        }

        .hero-description {
            position: relative;
            font-size: 16.5px;
            line-height: 1.75;
            color: var(--ink-500);
            max-width: 640px;
        }


        /* ====================================================
           SECTION HEADINGS
        ==================================================== */

        .section-heading {
            font-family: var(--font-display);
            font-size: 23px;
            font-weight: 600;
            color: var(--ink-900);
            margin-top: 30px;
            margin-bottom: 18px;
            padding-left: 16px;
            border-left: 4px solid var(--accent-coral);
        }


        /* ====================================================
           STREAMLIT COLUMNS
        ==================================================== */

        [data-testid="stHorizontalBlock"] {
            width: 100%;
            align-items: stretch;
        }

        [data-testid="column"] {
            min-width: 0 !important;
        }


        /* ====================================================
           BUTTONS  (pill-shaped, warm)
        ==================================================== */

        .stButton {
            width: 100%;
        }

        .stButton > button {
            width: 100%;
            min-height: 46px;

            border-radius: 999px;
            border: 1px solid var(--border-soft);

            background: var(--surface);
            color: var(--ink-700);

            font-family: var(--font-body);
            font-size: 14.5px;
            font-weight: 600;

            transition: all 0.25s ease;
        }

        .stButton > button:hover {
            background: linear-gradient(135deg, var(--accent-coral) 0%, var(--accent-coral-deep) 100%);
            border-color: transparent;
            color: #ffffff;

            transform: translateY(-2px);
            box-shadow: 0 8px 20px var(--shadow-coral);
        }

        .stButton > button:focus-visible {
            outline: none;
            box-shadow: 0 0 0 3px rgba(139, 127, 217, 0.35);
        }


        /* ====================================================
           FEATURE CARDS
        ==================================================== */

        .feature-card {
            width: 100%;
            min-height: 205px;

            box-sizing: border-box;

            background: var(--surface);

            border: 1px solid var(--border-soft);
            border-radius: 22px;

            padding: 30px;
            margin-bottom: 10px;

            box-shadow: 0 8px 24px rgba(44, 37, 66, 0.05);

            transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;

            display: flex;
            flex-direction: column;
        }

        .feature-card:hover {
            transform: translateY(-4px);
            border-color: var(--accent-violet);
            box-shadow: 0 16px 36px var(--shadow-violet);
        }

        .feature-icon {
            font-size: 26px;
            line-height: 1;
            margin-bottom: 18px;

            width: 52px;
            height: 52px;
            display: flex;
            align-items: center;
            justify-content: center;

            border-radius: 16px;
            background: linear-gradient(135deg, var(--surface-soft) 0%, #fdeef6 100%);
        }

        .feature-title {
            font-family: var(--font-display);
            font-size: 19px;
            font-weight: 600;
            color: var(--ink-900);
            margin-bottom: 9px;
        }

        .feature-description {
            font-size: 14px;
            line-height: 1.65;
            color: var(--ink-500);
        }

        .feature-card + div {
            margin-top: 6px;
        }


        /* ====================================================
           METRIC CARDS
        ==================================================== */

        div[data-testid="stMetric"] {
            background: var(--surface);

            border: 1px solid var(--border-soft);
            border-radius: 20px;

            padding: 18px 20px;
            min-height: 90px;

            box-shadow: 0 6px 20px rgba(44, 37, 66, 0.04);
        }

        div[data-testid="stMetricLabel"] {
            color: var(--ink-500) !important;
            font-weight: 600;
        }

        div[data-testid="stMetricValue"] {
            font-family: var(--font-display) !important;
            color: var(--accent-violet-deep) !important;
            font-weight: 600 !important;
        }


        /* ====================================================
           REMEMBER CARD
        ==================================================== */

        .remember-card {
            width: 100%;
            box-sizing: border-box;

            display: flex;
            align-items: center;
            gap: 20px;

            background: linear-gradient(135deg, #fdeef6 0%, var(--surface-soft) 100%);

            border: 1px solid var(--border-soft);
            border-radius: 22px;

            padding: 24px 28px;
            margin-top: 32px;
        }

        .remember-icon {
            font-size: 28px;
            flex-shrink: 0;

            width: 54px;
            height: 54px;
            display: flex;
            align-items: center;
            justify-content: center;

            border-radius: 50%;
            background: var(--surface);
            box-shadow: 0 6px 16px var(--shadow-coral);
        }

        .remember-title {
            font-family: var(--font-display);
            font-size: 17px;
            font-weight: 600;
            color: var(--ink-900);
            margin-bottom: 5px;
        }

        .remember-text {
            font-size: 14px;
            line-height: 1.6;
            color: var(--ink-700);
        }


        /* ====================================================
           TEXT INPUTS
        ==================================================== */

        input, textarea {
            border-radius: 14px !important;
            border: 1px solid var(--border-soft) !important;
            font-family: var(--font-body) !important;
        }

        input:focus, textarea:focus {
            border-color: var(--accent-violet) !important;
            box-shadow: 0 0 0 3px rgba(139, 127, 217, 0.15) !important;
        }


        /* ====================================================
           SELECT BOX
        ==================================================== */

        div[data-baseweb="select"] > div {
            border-radius: 14px;
            border-color: var(--border-soft);
        }


        /* ====================================================
           DIVIDERS
        ==================================================== */

        hr {
            border-color: var(--border-soft);
        }


        /* ====================================================
           INFO BOX (sidebar support message)
        ==================================================== */

        div[data-testid="stAlert"] {
            border-radius: 16px;
            background: var(--surface-soft) !important;
            border: 1px solid var(--border-soft) !important;
        }


        /* ====================================================
           SCROLLBAR
        ==================================================== */

        ::-webkit-scrollbar {
            width: 8px;
        }

        ::-webkit-scrollbar-track {
            background: transparent;
        }

        ::-webkit-scrollbar-thumb {
            background: var(--border-soft);
            border-radius: 10px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: var(--accent-violet);
        }


        /* ====================================================
           PAGE HEADER  (chat / journal / insights)
        ==================================================== */

        .chat-header {
            text-align: center;
            padding: 10px 20px 34px 20px;
        }

        .chat-header-icon {
            width: 64px;
            height: 64px;
            margin: 0 auto 16px auto;

            display: flex;
            align-items: center;
            justify-content: center;

            font-size: 30px;
            border-radius: 50%;

            background: linear-gradient(135deg, var(--surface-soft) 0%, #fdeef6 100%);
            box-shadow: 0 8px 22px var(--shadow-violet);
        }

        .chat-header h1 {
            font-family: var(--font-display) !important;
            font-size: 32px !important;
            color: var(--ink-900) !important;
            margin-bottom: 8px !important;
        }

        .chat-header p {
            font-size: 15.5px;
            color: var(--ink-500);
            max-width: 480px;
            margin: 0 auto;
            line-height: 1.6;
        }


        /* ====================================================
           SECTION TITLE  (inline variant of section-heading)
        ==================================================== */

        .section-title {
            font-family: var(--font-display);
            font-size: 20px;
            font-weight: 600;
            color: var(--ink-900);
            margin-top: 26px;
            margin-bottom: 14px;
            padding-left: 14px;
            border-left: 4px solid var(--accent-violet);
        }


        /* ====================================================
           CHAT BUBBLES
        ==================================================== */

        .message-name {
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 0.4px;
            margin-bottom: 5px;
            opacity: 0.75;
        }

        .user-message {
            max-width: 78%;
            margin: 0 0 14px auto;

            background: linear-gradient(135deg, var(--accent-coral) 0%, var(--accent-coral-deep) 100%);
            color: #ffffff;

            border-radius: 20px 20px 4px 20px;
            padding: 14px 20px;

            font-size: 14.5px;
            line-height: 1.6;

            box-shadow: 0 8px 20px var(--shadow-coral);
        }

        .user-message .message-name {
            color: rgba(255, 255, 255, 0.85);
        }

        .ai-message {
            max-width: 78%;
            margin: 0 auto 14px 0;

            background: var(--surface);
            color: var(--ink-700);
            border: 1px solid var(--border-soft);

            border-radius: 20px 20px 20px 4px;
            padding: 14px 20px;

            font-size: 14.5px;
            line-height: 1.6;

            box-shadow: 0 6px 18px rgba(44, 37, 66, 0.05);
        }

        .ai-message .message-name {
            color: var(--accent-violet-deep);
        }

        div[data-testid="stChatInput"] {
            border-radius: 18px;
        }

        div[data-testid="stChatInput"] textarea {
            font-family: var(--font-body) !important;
        }


        /* ====================================================
           STAT CARDS  (insights page)
        ==================================================== */

        .stat-card {
            width: 100%;
            box-sizing: border-box;
            text-align: center;

            background: var(--surface);
            border: 1px solid var(--border-soft);
            border-radius: 20px;

            padding: 26px 20px;
            margin-bottom: 10px;

            box-shadow: 0 8px 22px rgba(44, 37, 66, 0.05);
        }

        .stat-number {
            font-family: var(--font-display);
            font-size: 34px;
            font-weight: 600;
            color: var(--accent-violet-deep);
            line-height: 1.1;
            margin-bottom: 6px;
        }

        .stat-label {
            font-size: 13.5px;
            font-weight: 600;
            color: var(--ink-500);
        }


        /* ====================================================
           QUOTE CARD  (insights page)
        ==================================================== */

        .quote-card {
            width: 100%;
            box-sizing: border-box;

            display: flex;
            align-items: flex-start;
            gap: 20px;

            background: linear-gradient(135deg, var(--surface-soft) 0%, #fdeef6 100%);
            border: 1px solid var(--border-soft);
            border-radius: 22px;

            padding: 28px 30px;
            margin-top: 26px;
        }

        .quote-icon {
            font-size: 26px;
            flex-shrink: 0;

            width: 54px;
            height: 54px;
            display: flex;
            align-items: center;
            justify-content: center;

            border-radius: 50%;
            background: var(--surface);
            box-shadow: 0 6px 16px var(--shadow-violet);
        }

        .quote-card h3 {
            font-size: 18px !important;
            margin-bottom: 6px !important;
        }

        .quote-card p {
            font-size: 14px;
            line-height: 1.65;
            color: var(--ink-700);
            margin: 0;
        }


        /* ====================================================
           MOOD CARDS  (mood check-in page)
        ==================================================== */

        .mood-card {
            width: 100%;
            box-sizing: border-box;
            text-align: center;

            background: var(--surface);
            border: 1px solid var(--border-soft);
            border-radius: 18px;

            padding: 20px 10px 14px 10px;
            margin-bottom: 8px;

            transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
        }

        .mood-card:hover {
            transform: translateY(-3px);
            border-color: var(--accent-violet);
            box-shadow: 0 10px 24px var(--shadow-violet);
        }

        .mood-emoji {
            font-size: 32px;
            line-height: 1;
            margin-bottom: 8px;
        }

        .mood-title {
            font-size: 13.5px;
            font-weight: 600;
            color: var(--ink-700);
        }

        .mood-card-selected {
            border-color: var(--accent-violet);
            background: linear-gradient(135deg, var(--surface-soft) 0%, #fdeef6 100%);
            box-shadow: 0 10px 24px var(--shadow-violet);
        }


        /* ====================================================
           WELLNESS CARDS  (wellness activities page)
        ==================================================== */

        .wellness-card {
            width: 100%;
            box-sizing: border-box;

            background: var(--surface);
            border: 1px solid var(--border-soft);
            border-radius: 22px;

            padding: 28px;
            margin-bottom: 10px;

            box-shadow: 0 8px 24px rgba(44, 37, 66, 0.05);
            transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
        }

        .wellness-card:hover {
            transform: translateY(-4px);
            border-color: var(--accent-violet);
            box-shadow: 0 16px 36px var(--shadow-violet);
        }

        .wellness-icon {
            font-size: 26px;
            line-height: 1;
            margin-bottom: 14px;

            width: 52px;
            height: 52px;
            display: flex;
            align-items: center;
            justify-content: center;

            border-radius: 16px;
            background: linear-gradient(135deg, var(--surface-soft) 0%, #fdeef6 100%);
        }

        .wellness-card h2 {
            font-size: 19px !important;
            margin-bottom: 8px !important;
        }

        .wellness-card p {
            font-size: 14px;
            line-height: 1.6;
            color: var(--ink-500);
            margin-bottom: 12px;
        }

        .wellness-card strong {
            font-size: 13px;
            color: var(--accent-violet-deep);
        }


        /* ====================================================
           5-4-3-2-1 SENSE STEPS  (mindfulness exercise)
        ==================================================== */

        .sense-step {
            display: flex;
            align-items: center;
            gap: 16px;

            background: var(--surface);
            border: 1px solid var(--border-soft);
            border-radius: 16px;

            padding: 14px 18px;
            margin: 8px 0;
        }

        .sense-number {
            font-family: var(--font-display);
            font-size: 24px;
            font-weight: 600;
            color: var(--accent-coral-deep);
            flex-shrink: 0;
            width: 30px;
        }

        .sense-text {
            font-size: 14.5px;
            color: var(--ink-700);
        }


        /* ====================================================
           RESPONSIVE DESIGN
        ==================================================== */

        @media (max-width: 1000px) {

            .main .block-container {
                padding-left: 1.5rem;
                padding-right: 1.5rem;
            }

            .hero-card {
                padding: 36px 32px;
            }

            .hero-title {
                font-size: 34px;
            }

        }


        @media (max-width: 768px) {

            .main .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
            }

            .hero-card {
                padding: 30px 26px;
                border-radius: 22px;
            }

            .hero-title {
                font-size: 29px;
            }

            .hero-description {
                font-size: 15px;
            }

            .section-heading {
                font-size: 20px;
            }

            .feature-card {
                min-height: 180px;
                padding: 24px;
            }

            .feature-title {
                font-size: 17px;
            }

            .feature-description {
                font-size: 13px;
            }

            .chat-header h1 {
                font-size: 26px !important;
            }

            .user-message,
            .ai-message {
                max-width: 92%;
            }

        }

        </style>
        """,
        unsafe_allow_html=True
    )