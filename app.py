"""
Charlone Gianne V. Cruz — Personal Autobiography & Portfolio
Course: CSIT 349 · Applied AI
Institution: Cebu Institute of Technology – University (CIT-U)
Degree: 3rd Year Bachelor of Science in Computer Science (BSCS)
Theme: Naturalist Botanical & Avian Field Guide (High-Contrast, Rich Dark & Light Modes, No Emojis)
"""

import os
import streamlit as st
import pandas as pd
import altair as alt

# -----------------------------------------------------------------------------
# 1. Page Configuration
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Charlone Gianne V. Cruz | Portfolio & Autobiography",
    page_icon="assets/profile_avatar.svg",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# 2. Vector SVG Icons (Zero Emojis)
# -----------------------------------------------------------------------------
def get_svg_icon(name: str, width: int = 16, height: int = 16, color: str = "currentColor") -> str:
    """Returns clean inline SVGs for botanical and field icons."""
    icons = {
        "leaf": f'''<svg width="{width}" height="{height}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: -2px; display: inline-block;"><path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/></svg>''',
        "feather": f'''<svg width="{width}" height="{height}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: -2px; display: inline-block;"><path d="M20.24 12.24a6 6 0 0 0-8.49-8.49L5 10.5V19h8.5z"/><line x1="16" y1="8" x2="2" y2="22"/><line x1="17.5" y1="15" x2="9" y2="15"/></svg>''',
        "compass": f'''<svg width="{width}" height="{height}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: -2px; display: inline-block;"><circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/></svg>''',
        "award": f'''<svg width="{width}" height="{height}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: -2px; display: inline-block;"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg>''',
        "mail": f'''<svg width="{width}" height="{height}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: -2px; display: inline-block;"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>''',
        "code": f'''<svg width="{width}" height="{height}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: -2px; display: inline-block;"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>''',
        "music": f'''<svg width="{width}" height="{height}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: -2px; display: inline-block;"><path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/></svg>'''
    }
    return icons.get(name, "")

# -----------------------------------------------------------------------------
# 3. De-cluttered Sidebar
# -----------------------------------------------------------------------------
with st.sidebar:
    avatar_path = os.path.join(os.path.dirname(__file__), "assets", "profile_avatar.svg")
    if os.path.exists(avatar_path):
        st.image(avatar_path, use_container_width=True)
    
    st.markdown("""
    <div style="text-align: center; margin-top: 4px; margin-bottom: 12px;">
        <h3 style="margin-bottom: 2px; font-size: 1.25rem;">Charlone Gianne V. Cruz</h3>
        <p style="font-size: 0.86rem; margin-bottom: 0;">3rd Year BSCS · CIT-U</p>
        <p style="font-size: 0.8rem; margin-bottom: 0;"><strong>Course:</strong> CSIT 349 · Applied AI</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Theme Selection (Clean 2-Option Radio)
    theme_choice = st.radio(
        "Theme Palette:",
        options=["Canopy Dark (Deep Forest)", "Parchment Light (Warm Paper)"],
        index=0,
        horizontal=True
    )
    
    # Domain Filter
    sidebar_domain_filter = st.selectbox(
        "Highlight Focus:",
        options=["All Domains", "Machine Learning & AI", "Community & Social Impact"],
        index=0
    )

# -----------------------------------------------------------------------------
# 4. Rich, Atmospheric CSS Injection (Fixes White-on-White, Expander & Inputs)
# -----------------------------------------------------------------------------
is_dark = ("Canopy Dark" in theme_choice)

if is_dark:
    # Rich, deep forest dark theme with moss, amber, and luminous sage
    css_tokens = """
    :root {
        --canvas-bg: #0B130E;
        --sidebar-bg: #070D09;
        --card-bg: #111C15;
        --card-border: #1E3325;
        --card-hover-border: #2D4C38;
        --input-bg: #14221A;
        --text-primary: #E5EDE8;
        --text-muted: #8EA395;
        --heading-color: #7EC99E;
        --accent-color: #E5A869;
        --tag-bg: #16261D;
        --tag-color: #A3DFBC;
        --tag-border: #243F2E;
        --quote-border: #529671;
        --quote-text: #C7D8CE;
        --btn-bg: #15241C;
        --btn-text: #8CD6AB;
        --btn-border: #264230;
    }
    """
else:
    # Warm naturalist parchment light theme
    css_tokens = """
    :root {
        --canvas-bg: #FAF7F2;
        --sidebar-bg: #F4EFE6;
        --card-bg: #FFFFFF;
        --card-border: #E2DDD3;
        --card-hover-border: #C4BCAC;
        --input-bg: #FFFFFF;
        --text-primary: #1C251F;
        --text-muted: #5A6A60;
        --heading-color: #173C29;
        --accent-color: #B45309;
        --tag-bg: #EBF2ED;
        --tag-color: #173C29;
        --tag-border: #D1E2D6;
        --quote-border: #2E5A44;
        --quote-text: #37483C;
        --btn-bg: #F2ECE1;
        --btn-text: #173C29;
        --btn-border: #D8D0C2;
    }
    """

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400;1,6..72,500&family=Plus+Jakarta+Sans:wght@400;500;600&display=swap');

{css_tokens}

/* Root Page Canvas & Typography */
.stApp, [data-testid="stAppViewContainer"] {{
    background-color: var(--canvas-bg) !important;
    font-family: 'Newsreader', Georgia, serif;
    color: var(--text-primary);
}}

[data-testid="stSidebar"] {{
    background-color: var(--sidebar-bg) !important;
}}

/* Clean Headings */
h1, h2, h3, h4, .stTitle, [data-testid="stHeading"] {{
    font-family: 'Newsreader', Georgia, serif !important;
    font-weight: 600 !important;
    color: var(--heading-color) !important;
    letter-spacing: -0.01em;
}}

.stApp p, .stApp span, .stApp label, .stMarkdown {{
    color: var(--text-primary);
}}

/* Custom Cards */
.botanical-card {{
    background-color: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 10px;
    padding: 22px 24px;
    margin-bottom: 20px;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.05);
    transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.25s ease, border-color 0.2s ease;
    display: flex !important;
    flex-direction: column !important;
    justify-content: space-between !important;
    height: 100% !important;
    box-sizing: border-box !important;
}}
.botanical-card:hover {{
    border-color: var(--card-hover-border);
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
}}

/* Card Internal Layout & Apple Alignment */
.card-content-body {{
    flex: 1 1 auto;
    display: flex;
    flex-direction: column;
}}
.card-title {{
    margin-top: 6px;
    margin-bottom: 6px;
    font-size: 1.22rem !important;
    line-height: 1.35 !important;
    letter-spacing: -0.015em !important;
    color: var(--heading-color) !important;
}}
.card-accolade {{
    font-family: -apple-system, BlinkMacSystemFont, 'Plus Jakarta Sans', sans-serif;
    font-size: 0.82rem;
    color: var(--accent-color);
    font-weight: 600;
    margin-bottom: 8px;
    line-height: 1.4;
}}
.card-role {{
    font-size: 0.88rem;
    color: var(--text-muted);
    margin-bottom: 12px;
}}
.card-summary {{
    font-size: 0.92rem;
    line-height: 1.6;
    margin-bottom: 14px;
    color: var(--text-primary);
}}
.card-tools {{
    margin-bottom: 16px;
}}
.card-content-footer {{
    margin-top: auto;
    padding-top: 14px;
    border-top: 1px solid var(--card-border);
}}
.card-link-wrapper {{
    margin-bottom: 8px;
}}
.card-repo-link {{
    font-family: -apple-system, BlinkMacSystemFont, 'Plus Jakarta Sans', sans-serif;
    font-size: 0.84rem;
    color: var(--heading-color);
    font-weight: 600;
    text-decoration: underline;
    text-underline-offset: 3px;
    transition: color 0.15s ease;
}}
.card-repo-link:hover {{
    color: var(--accent-color);
}}

/* Apple Details / Disclosure inside Card */
.apple-details {{
    background-color: var(--tag-bg);
    border: 1px solid var(--tag-border);
    border-radius: 6px;
    padding: 2px 10px;
    margin-top: 8px;
    transition: background-color 0.2s ease;
}}
.apple-summary {{
    list-style: none;
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-family: -apple-system, BlinkMacSystemFont, 'Plus Jakarta Sans', sans-serif;
    font-size: 0.8rem;
    font-weight: 600;
    color: var(--heading-color);
    padding: 8px 2px;
    user-select: none;
}}
.apple-summary::-webkit-details-marker {{
    display: none;
}}
.apple-summary .apple-chevron {{
    font-size: 0.95rem;
    font-weight: bold;
    color: var(--text-muted);
    transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}}
.apple-details[open] .apple-summary .apple-chevron {{
    transform: rotate(90deg);
}}
.apple-details-content {{
    padding: 6px 2px 8px 2px;
    border-top: 1px solid var(--card-border);
    margin-top: 2px;
    animation: appleDetailsFade 0.2s cubic-bezier(0.16, 1, 0.3, 1);
}}
@keyframes appleDetailsFade {{
    from {{ opacity: 0; transform: translateY(-4px); }}
    to {{ opacity: 1; transform: translateY(0); }}
}}
.metric-row {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 4px 0;
    font-size: 0.8rem;
}}
.metric-key {{
    color: var(--text-muted);
    font-weight: 500;
}}
.metric-val {{
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, monospace;
    font-size: 0.78rem;
    color: var(--heading-color);
    font-weight: 600;
    background-color: var(--card-bg);
    padding: 2px 6px;
    border-radius: 4px;
    border: 1px solid var(--card-border);
}}

/* Grid Stretch Alignment across Columns */
div[data-testid="stHorizontalBlock"] {{
    align-items: stretch !important;
}}
div[data-testid="stHorizontalBlock"] > div[data-testid="column"] {{
    display: flex !important;
    flex-direction: column !important;
}}
div[data-testid="stHorizontalBlock"] > div[data-testid="column"] > div[data-testid="stVerticalBlock"] {{
    display: flex !important;
    flex-direction: column !important;
    flex: 1 1 auto !important;
    height: 100% !important;
}}
div[data-testid="stHorizontalBlock"] > div[data-testid="column"] > div[data-testid="stVerticalBlock"] > div[data-testid="element-container"],
div[data-testid="stHorizontalBlock"] > div[data-testid="column"] > div[data-testid="stVerticalBlock"] > div[data-testid="stMarkdownContainer"] {{
    display: flex !important;
    flex-direction: column !important;
    flex: 1 1 auto !important;
    height: 100% !important;
}}

/* Specimen Tags */
.tag-pill {{
    display: inline-block;
    background-color: var(--tag-bg);
    color: var(--tag-color);
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 0.74rem;
    font-weight: 600;
    padding: 3px 9px;
    border-radius: 20px;
    margin-right: 6px;
    margin-bottom: 6px;
    border: 1px solid var(--tag-border);
}}

.tag-accent {{
    display: inline-block;
    background-color: transparent;
    color: var(--accent-color);
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 0.74rem;
    font-weight: 600;
    padding: 2px 8px;
    border-radius: 20px;
    margin-right: 6px;
    margin-bottom: 6px;
    border: 1px solid var(--accent-color);
}}

/* Editorial Quote */
.editorial-quote {{
    border-left: 3px solid var(--quote-border);
    padding-left: 18px;
    margin: 16px 0;
    font-style: italic;
    color: var(--quote-text);
    font-size: 1.1rem;
    line-height: 1.6;
}}

/* Fix Streamlit Expanders (Prevents White-on-White Headers) */
[data-testid="stExpander"] {{
    background-color: var(--card-bg) !important;
    border: 1px solid var(--card-border) !important;
    border-radius: 8px !important;
    margin-bottom: 12px !important;
}}
[data-testid="stExpander"] details {{
    background-color: var(--card-bg) !important;
    color: var(--text-primary) !important;
}}
[data-testid="stExpander"] summary {{
    background-color: var(--card-bg) !important;
    color: var(--heading-color) !important;
    border-radius: 7px !important;
    padding: 12px 16px !important;
}}
[data-testid="stExpander"] summary p, [data-testid="stExpander"] summary span {{
    color: var(--heading-color) !important;
    font-weight: 600 !important;
}}
[data-testid="stExpander"] summary:hover {{
    color: var(--accent-color) !important;
}}
[data-testid="stExpander"] summary:hover p {{
    color: var(--accent-color) !important;
}}

/* Fix Form Inputs, Selectboxes & Multiselects (High Contrast) */
div[data-baseweb="select"] > div, div[data-baseweb="base-input"] {{
    background-color: var(--input-bg) !important;
    border-color: var(--card-border) !important;
    color: var(--text-primary) !important;
    border-radius: 6px !important;
}}
div[data-baseweb="select"] span, div[data-baseweb="select"] div {{
    color: var(--text-primary) !important;
}}
div[data-baseweb="input"] input, div[data-baseweb="textarea"] textarea {{
    background-color: var(--input-bg) !important;
    color: var(--text-primary) !important;
    border-color: var(--card-border) !important;
}}

/* Fix Buttons */
div.stButton > button, div[data-testid="stFormSubmitButton"] > button {{
    background-color: var(--btn-bg) !important;
    color: var(--btn-text) !important;
    border: 1px solid var(--btn-border) !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 600 !important;
    border-radius: 6px !important;
    padding: 8px 16px !important;
    transition: all 0.2s ease !important;
}}
div.stButton > button:hover, div[data-testid="stFormSubmitButton"] > button:hover {{
    border-color: var(--accent-color) !important;
    color: var(--accent-color) !important;
}}

/* Tabs Layout */
.stTabs [data-baseweb="tab-list"] {{
    gap: 8px;
    border-bottom: 1px solid var(--card-border);
    padding-bottom: 4px;
}}
.stTabs [data-baseweb="tab"] {{
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 500 !important;
    color: var(--text-muted) !important;
    border-radius: 6px 6px 0 0;
    padding: 8px 16px;
}}
.stTabs [aria-selected="true"] {{
    color: var(--heading-color) !important;
    font-weight: 600 !important;
    border-bottom: 2px solid var(--heading-color) !important;
}}

/* Clean Full-Text Specimen Table Styling */
[data-testid="stTable"] {{
    width: 100% !important;
    overflow-x: auto !important;
    border-radius: 8px !important;
    border: 1px solid var(--card-border) !important;
    background-color: var(--card-bg) !important;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.04) !important;
    margin-top: 10px !important;
    margin-bottom: 20px !important;
}}
[data-testid="stTable"] table {{
    width: 100% !important;
    border-collapse: collapse !important;
    background-color: var(--card-bg) !important;
    color: var(--text-primary) !important;
    font-size: 0.9rem !important;
}}
[data-testid="stTable"] th {{
    background-color: var(--tag-bg) !important;
    color: var(--heading-color) !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.82rem !important;
    padding: 12px 16px !important;
    border-bottom: 1px solid var(--card-border) !important;
    text-align: left !important;
    letter-spacing: 0.02em !important;
}}
[data-testid="stTable"] td {{
    color: var(--text-primary) !important;
    padding: 12px 16px !important;
    border-bottom: 1px solid var(--card-border) !important;
    vertical-align: top !important;
    line-height: 1.55 !important;
    white-space: normal !important;
    word-break: normal !important;
}}
[data-testid="stTable"] tr:last-child td {{
    border-bottom: none !important;
}}
[data-testid="stTable"] tr:hover td {{
    background-color: rgba(255, 255, 255, 0.03) !important;
}}
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 5. Session State Initialization
# -----------------------------------------------------------------------------
if "guestbook" not in st.session_state:
    st.session_state["guestbook"] = [
        {
            "sender": "Prof. Applied AI",
            "type": "Academic Review",
            "message": "Strong integration of LightGBM and 1D Temporal CNN models for real-world impact.",
            "date": "Today, 10:15 AM"
        }
    ]

# -----------------------------------------------------------------------------
# 6. Real Technical Data (Clean 3-Column Inventory: Domain, Skill, Project)
# -----------------------------------------------------------------------------
skills_data = pd.DataFrame([
    {
        "Domain": "Machine Learning & AI",
        "Skill / Technology": "LightGBM",
        "Real-World Application / Project": "PAROLA — Dual predictive pipelines forecasting demersal and pelagic fisheries (PSC Region VII Top 25 Finalist)"
    },
    {
        "Domain": "Machine Learning & AI",
        "Skill / Technology": "1D Temporal CNN & MLP",
        "Real-World Application / Project": "PhysioCGM Telemetry — Nocturnal hypoglycemia detection using continuous smartwatch physiological sensor signals"
    },
    {
        "Domain": "Machine Learning & AI",
        "Skill / Technology": "PyTorch & Scikit-learn",
        "Real-World Application / Project": "Exploratory signal modeling, sequential trend feature engineering, and baseline validation"
    },
    {
        "Domain": "Computer Vision",
        "Skill / Technology": "OpenCV (Java Interface)",
        "Real-World Application / Project": "IMentia — Real-time camera facial recognition and contextual memory prompt assistant for dementia patients"
    },
    {
        "Domain": "Natural Language Processing",
        "Skill / Technology": "SpeechRecognition & AST Parsing",
        "Real-World Application / Project": "SpeechToCode — Error-tolerant voice-to-code synthesis formatting natural speech into structured syntax"
    },
    {
        "Domain": "Web Architecture",
        "Skill / Technology": "Python Django (MVT)",
        "Real-World Application / Project": "LantaWires — Scalable web platform with role-based authentication and relational database management"
    },
    {
        "Domain": "Web Architecture",
        "Skill / Technology": "C# Blazor WebAssembly",
        "Real-World Application / Project": "CineTerra & OurDriedFish — Reactive single-page client applications running native C# in the browser"
    },
    {
        "Domain": "Desktop Software",
        "Skill / Technology": "Java & JavaFX / Swing",
        "Real-World Application / Project": "+inHealth & IMentia — Desktop ergonomic activity monitor and assistive healthcare interfaces"
    },
    {
        "Domain": "Campus Infrastructure",
        "Skill / Technology": "PHP & MySQL",
        "Real-World Application / Project": "WildGuard — Campus security reporting, visitor logging, and incident access tracking system"
    },
    {
        "Domain": "Game Development",
        "Skill / Technology": "Game Jam Logic Engine",
        "Real-World Application / Project": "Sugbuanon Saga: Banhwa — Game Jam 2025 narrative adventure celebrating Cebuano folklore"
    }
])

projects_list = [
    {
        "rank": 1,
        "title": "PAROLA — Intelligent Marine Catch Prediction System",
        "category": "Machine Learning & AI",
        "role": "Lead Machine Learning Engineer (Team Tiki)",
        "accolade": "Top 25 Regional Finalist & Best Logo Design Award · Philippine Startup Challenge (PSC) Region VII",
        "tools": ["Python", "LightGBM", "Pandas", "Scikit-learn", "Geospatial Telemetry"],
        "summary": "Designed dual specialized gradient-boosted decision tree models using LightGBM, training distinct predictive pipelines for demersal (bottom-dwelling) and pelagic (open-water) fish species. Correlates ocean currents, sea-surface temperature, and seasonal coordinates to pinpoint sustainable, fuel-saving fishing zones for artisanal fishermen in Region VII.",
        "repo": "https://github.com/Gianne818/Parola_PSC",
        "metrics": {"Primary Model": "Dual LightGBM", "Target Species": "Demersal + Pelagic", "Scope": "Region VII Fisheries"}
    },
    {
        "rank": 2,
        "title": "Nocturnal Hypoglycemia Detection via Wearable CGM Telemetry",
        "category": "Machine Learning & AI",
        "role": "Lead AI Researcher & Data Analyst",
        "accolade": "Applied AI & Biomedical Time-Series Research",
        "tools": ["Python", "PyTorch", "1D Temporal CNN", "MLP", "PhysioCGM Dataset"],
        "summary": "Investigated whether non-invasive consumer smartwatches can reliably detect nocturnal hypoglycemia episodes before critical drops. Analyzed the PhysioCGM dataset, formulated signal augmentation, and engineered a sequential 1D Temporal CNN (TCN) capturing nocturnal physiological trends that outperform standard MLP baselines.",
        "repo": "https://github.com/Gianne818",
        "metrics": {"Architecture": "1D Temporal CNN", "Baseline": "Multi-Layer Perceptron", "Dataset": "PhysioCGM Multimodal"}
    },
    {
        "rank": 3,
        "title": "IMentia — AI Facial Recognition & Memory Recall Assistant",
        "category": "Assistive & Community",
        "role": "Computer Vision & AI Developer",
        "accolade": "Assistive Healthcare & Identity Retention Platform",
        "tools": ["Java", "Java Swing", "OpenCV (Java Interface)", "SQLite"],
        "summary": "Developed an assistive desktop healthcare platform for dementia and Alzheimer's patients. Uses a live camera feed and OpenCV facial recognition to identify visiting loved ones, instantly displaying relational context, conversation logs, and memory prompts to preserve emotional connection.",
        "repo": "https://github.com/Gianne818",
        "metrics": {"Modality": "Live Video Feed", "Engine": "OpenCV Java", "Focus": "Memory Retention"}
    },
    {
        "rank": 4,
        "title": "SpeechToCode — AI Voice-to-Code Synthesis Engine",
        "category": "Machine Learning & AI",
        "role": "AI Developer & NLP Engineer",
        "accolade": "Developer Accessibility & Voice Parsing",
        "tools": ["Python", "SpeechRecognition", "AST Parsing", "NLP"],
        "summary": "Translates spoken natural language into syntactically sound code structures. Built custom error-tolerant phonetic parsing to resolve homophones and syntax ambiguities even under noisy acoustic conditions.",
        "repo": "https://github.com/Gianne818",
        "metrics": {"Language": "Python", "Parsing": "Phonetic AST", "Input": "Acoustic Speech"}
    },
    {
        "rank": 5,
        "title": "LantaWires — Scalable Web Architecture Platform",
        "category": "Full-Stack & Systems",
        "role": "Full-Stack Backend Developer",
        "accolade": "Enterprise Web Platform Architecture",
        "tools": ["Python", "Django (MVT)", "PostgreSQL", "JavaScript"],
        "summary": "Architected a scalable, modular web application utilizing Django's Model-View-Template pattern, with secure role-based authentication, modular relational database models, and an intuitive administrative operations dashboard.",
        "repo": "https://github.com/Gianne818/LantaWires",
        "metrics": {"Framework": "Django MVT", "Database": "PostgreSQL / SQLite", "Architecture": "Modular Monolith"}
    },
    {
        "rank": 6,
        "title": "CineTerra — Cinematic Discovery & Media Platform",
        "category": "Full-Stack & Systems",
        "role": "Frontend Engineer",
        "accolade": "High-Performance Single-Page App",
        "tools": ["C#", ".NET", "Blazor WebAssembly", "Modern CSS"],
        "summary": "Constructed a responsive single-page cinema exploration interface executing client-side C# directly in the browser via Blazor WebAssembly, eliminating heavy JavaScript overhead while providing instant catalog filtering.",
        "repo": "https://github.com/Gianne818/CineTerra",
        "metrics": {"Runtime": "Blazor WebAssembly", "Language": "C# (.NET)", "Client": "Zero Heavy JS"}
    },
    {
        "rank": 7,
        "title": "OurDriedFish — Local Artisanal E-Commerce Platform",
        "category": "Full-Stack & Systems",
        "role": "Frontend Developer",
        "accolade": "Regional Artisanal Digitalization",
        "tools": ["C#", "Blazor WebAssembly", "Component CSS"],
        "summary": "Digital showcase platform celebrating Cebuano dried seafood producers (danggit, dried squid). Built with reactive Blazor component state and responsive UI to empower local micro-vendors.",
        "repo": "https://github.com/Gianne818/OurDriedFish",
        "metrics": {"Domain": "Cebuano Artisanal", "Framework": "Blazor Wasm", "State": "Reactive Components"}
    },
    {
        "rank": 8,
        "title": "+inHealth — Desktop Ergonomic Wellness & Activity Monitor",
        "category": "Assistive & Community",
        "role": "Software Developer",
        "accolade": "Preventative Ergonomics for Developers",
        "tools": ["Java", "JavaFX", "Desktop Event Hooks"],
        "summary": "Proactive desktop health monitor combating screen fatigue and sedentary habits through non-intrusive posture nudges, hydration reminders, and gentle ergonomic activity prompts.",
        "repo": "https://github.com/Gianne818",
        "metrics": {"Platform": "Desktop", "UI": "JavaFX", "Mission": "Sedentary Relief"}
    },
    {
        "rank": 9,
        "title": "WildGuard — Campus Security & Incident Reporting System",
        "category": "Full-Stack & Systems",
        "role": "Backend Developer",
        "accolade": "Campus Physical Infrastructure & Safety",
        "tools": ["PHP", "MySQL", "Apache", "Web Forms"],
        "summary": "Centralized reporting and visitor access management system for campus security personnel, handling visitor logs, incident reporting, and audit trails.",
        "repo": "https://github.com/Gianne818",
        "metrics": {"Stack": "LAMP (PHP/MySQL)", "Scope": "Campus Safety", "Audit": "Structured Relational"}
    },
    {
        "rank": 10,
        "title": "Sugbuanon Saga: Banhwa — Cultural Mythological Adventure",
        "category": "Assistive & Community",
        "role": "Game Logic & Narrative Developer",
        "accolade": "Game Jam 2025 Submission",
        "tools": ["Game Jam Framework", "2D Pixel Art", "Narrative State Engine"],
        "summary": "Story-driven adventure game celebrating Visayan and Cebuano folklore: when an ancient relic protecting Cebu shatters, the player reforges the artifact while navigating mythical creatures.",
        "repo": "https://github.com/Gianne818",
        "metrics": {"Theme": "Visayan Folklore", "Engine": "Game Jam 2025", "Story": "Relic Reforging"}
    }
]

# -----------------------------------------------------------------------------
# 7. Main Deck: Hero Header
# -----------------------------------------------------------------------------
col_hero_1, col_hero_2 = st.columns([3, 1])

with col_hero_1:
    st.title("Charlone Gianne V. Cruz")
    st.markdown("##### Full-Stack Developer · Machine Learning Researcher · AI Systems Architect")
    st.markdown("""
    **Cebu Institute of Technology – University (CIT-U)** &nbsp;|&nbsp; 
    **3rd Year BS Computer Science** &nbsp;|&nbsp; 
    **Course:** CSIT 349 · Applied AI
    """)
    st.markdown("""
    <div class="editorial-quote">
    "Rooted in compassion, guided by observation. I build intelligent systems that serve people—from predicting sustainable fishing grounds for local communities to detecting nocturnal glycemic drops through wearable telemetry."
    </div>
    """, unsafe_allow_html=True)

with col_hero_2:
    st.markdown(f"""
    <div class="botanical-card" style="text-align: center; padding: 18px 14px; margin-top: 14px;">
        <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 0.8rem; font-weight: 600; color: var(--heading-color); letter-spacing: 0.08em;">
            {get_svg_icon('leaf', 14, 14)} BOTANY &nbsp;·&nbsp; {get_svg_icon('feather', 14, 14)} BIRDS &nbsp;·&nbsp; {get_svg_icon('music', 14, 14)} MUSIC
        </div>
        <div style="font-size: 0.76rem; color: var(--text-muted); margin-top: 6px;">
            Core pursuits & life outside the terminal
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# -----------------------------------------------------------------------------
# 8. Curated Tabs
# -----------------------------------------------------------------------------
tab_bio, tab_skills, tab_projects, tab_dispatch = st.tabs([
    "Chapter I: Autobiography & Roots",
    "Chapter II: Technical Capabilities",
    "Chapter III: Project Portfolio",
    "Chapter IV: Dispatch & Inquiries"
])

# =============================================================================
# TAB 1: AUTOBIOGRAPHY & ROOTS
# =============================================================================
with tab_bio:
    st.header("Autobiography: Finding Rhythm Between Nature and Code")
    
    col_bio_left, col_bio_right = st.columns([2, 1])
    
    with col_bio_left:
        st.markdown("""
        I am a 20-year-old Computer Science undergraduate at **Cebu Institute of Technology – University (CIT-U)**. 
        My journey with technology has never been about code for code's sake. Instead, it has always been grounded 
        in a deep reverence for the living world—**the quiet patience of plants**, **the effortless aerodynamics of birds**, 
        **the expressive harmonies of music**, and an abiding conviction that computation must serve human dignity.
        
        ### Background & Early Inspirations
        Growing up, I was drawn to systems where small, deliberate choices produced emergent beauty. In music, a single shift 
        in voicing alters the emotional landscape of a piece. In botany, a plant senses light, gravity, and moisture to navigate 
        its environment with silent intelligence. When I encountered programming, I realized that algorithms are not cold 
        abstractions—they are dynamic structures through which we can solve tangible, human problems.
        
        ### Education & Academic Philosophy
        At CIT-U, pursuing my **BS in Computer Science**, I have focused heavily on bridging **theoretical mathematics and machine learning** 
        with **production-grade software engineering**. I believe an AI model is only as valuable as the real-world relief it brings 
        to someone's day-to-day struggle. Whether that means:
        - Giving artisanal fishermen actionable marine forecasts so they waste less fuel at sea (**PAROLA**),
        - Alerting individuals with diabetes to nocturnal hypoglycemia through smartwatch sensors before an episode becomes dangerous (**PhysioCGM Research**), or
        - Restoring dignity and memory recall to patients living with dementia through real-time facial recognition (**IMentia**).
        """)

    with col_bio_right:
        st.markdown(f"""
        <div class="botanical-card">
            <h4 style="margin-top: 0; color: var(--heading-color); font-size: 1.15rem;">
                {get_svg_icon('leaf', 16, 16)} Student Specimen Card
            </h4>
            <p style="font-size: 0.9rem; margin-bottom: 7px;"><strong>Full Name:</strong> Charlone Gianne V. Cruz</p>
            <p style="font-size: 0.9rem; margin-bottom: 7px;"><strong>Age:</strong> 20</p>
            <p style="font-size: 0.9rem; margin-bottom: 7px;"><strong>Institution:</strong> CIT-U, Cebu City</p>
            <p style="font-size: 0.9rem; margin-bottom: 7px;"><strong>Program:</strong> 3rd Year BSCS</p>
            <p style="font-size: 0.9rem; margin-bottom: 7px;"><strong>Course:</strong> CSIT 349 · Applied AI</p>
            <p style="font-size: 0.9rem; margin-bottom: 7px;"><strong>Primary Role:</strong> ML Researcher & Full-Stack Dev</p>
            <p style="font-size: 0.9rem; margin-bottom: 0;"><strong>Core Passions:</strong> Music · Birds · Botany · Social Impact</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Reveal Guiding Philosophy", use_container_width=True):
            st.info("*'The true elegance of an algorithm is not measured by its complexity, but by the quiet burden it lifts from another human being.'*")

    st.markdown("---")
    
    # Life Allocation Chart (Rubric: Chart Component)
    st.subheader("Current Life Focus & Time Allocation")
    st.write(
        "A snapshot of how my days are balanced between academics, applied AI research, and personal grounding:"
    )
    
    life_focus_data = pd.DataFrame([
        {"Pursuit": "Others", "Percentage": 35, "Category": "Others"},
        {"Pursuit": "Academics", "Percentage": 30, "Category": "Academics"},
        {"Pursuit": "Extracurriculars", "Percentage": 15, "Category": "Extracurriculars"},
        {"Pursuit": "Pet Birds", "Percentage": 15, "Category": "Pet Birds"},
        {"Pursuit": "Plants", "Percentage": 5, "Category": "Plants"}
    ])
    life_focus_data["Label"] = life_focus_data["Percentage"].apply(lambda x: f"{x}%")
    
    if is_dark:
        chart_palette = ['#E5A869', '#7EC99E', '#529671', '#407559', '#2E5A44']
        text_color = '#E2E8F0'
    else:
        chart_palette = ['#C27D38', '#1B3B2B', '#2D5A43', '#406B52', '#6E8F7A']
        text_color = '#1C251F'
        
    base = alt.Chart(life_focus_data).encode(
        y=alt.Y(
            'Pursuit:N',
            sort=['Others', 'Academics', 'Extracurriculars', 'Pet Birds', 'Plants'],
            title=None,
            axis=alt.Axis(
                labelLimit=300,
                labelPadding=16,
                labelColor=text_color,
                tickColor='transparent',
                domainColor='transparent'
            )
        )
    )
    
    bars = base.mark_bar(cornerRadiusEnd=6, height=24).encode(
        x=alt.X(
            'Percentage:Q',
            title='Allocation of Active Time (%)',
            scale=alt.Scale(domain=[0, 42]),
            axis=alt.Axis(
                labelColor=text_color,
                titleColor=text_color,
                gridColor='rgba(255, 255, 255, 0.08)' if is_dark else 'rgba(0, 0, 0, 0.06)',
                domainColor='rgba(255, 255, 255, 0.15)' if is_dark else 'rgba(0, 0, 0, 0.15)'
            )
        ),
        color=alt.Color('Pursuit:N', scale=alt.Scale(range=chart_palette), legend=None),
        tooltip=['Pursuit', 'Percentage']
    )
    
    text = base.mark_text(
        align='left',
        baseline='middle',
        dx=6,
        font='Plus Jakarta Sans',
        fontSize=11,
        fontWeight=600,
        color=text_color
    ).encode(
        x='Percentage:Q',
        text='Label:N'
    )
    
    chart = (bars + text).properties(
        height=240,
        padding={'left': 35, 'top': 10, 'right': 35, 'bottom': 10}
    ).configure(
        background='transparent'
    ).configure_axis(
        labelFont='Plus Jakarta Sans',
        titleFont='Newsreader',
        labelFontSize=11,
        titleFontSize=12,
        grid=False
    ).configure_view(
        strokeWidth=0,
        fill='transparent'
    )
    st.altair_chart(chart, use_container_width=True, theme=None)

    st.markdown("---")
    st.subheader("Key Academic & Competition Milestones")
    
    with st.expander("October 2026: Philippine Startup Challenge (PSC) Region VII — Top 25 Finalist & Best Logo Design", expanded=True):
        st.write("""
        Competed at the DICT Philippine Startup Challenge XI / XII Regional Finals at Bai Hotel, Mandaue City with **Team Tiki**. 
        Led the Machine Learning modeling for **PAROLA**, an intelligent marine catch prediction platform. Recognized among the 
        **Top 25 regional startups** and awarded the **Best Logo Design Award** for blending nautical lighthouse symbolism with modern conservation tech.
        """)
        
    with st.expander("2026: AIFEST AI Hackathon Competency Series"):
        st.write("""
        Participated across intensive technical and design tracks:
        - **Workshop 1:** Human-Centered AI Design & Problem Discovery.
        - **Workshop 2:** Technical System Architecture & Scalable Model Pipelines.
        - **Webinar 3:** Agile Pitching, Venture Strategy, and Sustainable Deployment.
        """)

    with st.expander("December 2025: AI Ready ASEAN Certification (ASEAN Foundation & Google.org)"):
        st.write("""
        Earned verified credential covering ethical artificial intelligence deployment, prompt engineering, generative fundamentals, 
        and responsible technological integration across Southeast Asia.
        """)

# =============================================================================
# TAB 2: TECHNICAL CAPABILITIES & SKILLS
# =============================================================================
with tab_skills:
    st.header("Technical Capabilities & Engineering Overview")
    
    # Grounded Synthesis Paragraph
    st.markdown("""
    My technical foundation centers on **Applied Machine Learning**, **Biomedical Sensor Telemetry**, and **Full-Stack Application Architecture**. 
    Rather than treating machine learning models as isolated notebooks, I focus on integrating predictive models directly into production environments:
    
    - In **Classical Machine Learning & GBDTs**, I specialize in gradient-boosted decision trees using **LightGBM**, architecting multi-pipeline systems such as predicting separate demersal and pelagic marine species for regional fisheries.
    - In **Deep Learning & Biomedical Time-Series**, I analyze continuous physiological signals from wearable sensors (e.g., the PhysioCGM dataset), progressing from baseline Multilayer Perceptrons (MLPs) to sequential **1D Temporal Convolutional Neural Networks (1D CNNs)** to identify nocturnal glycemic patterns.
    - In **Software Systems & Web Architecture**, I build robust backends with **Python Django (MVT)** and responsive client-side interfaces using **C# Blazor WebAssembly**, supported by **Java/OpenCV** for computer vision applications.
    """)
    
    st.markdown("---")
    
    # Clean 3-Column Technical Inventory Table (Rubric: Table Component)
    st.subheader("Technical Inventory: Domain, Skills & Real-World Implementations")
    st.caption("All real-world implementations and technical outcomes displayed in full without truncation:")
    
    col_tab_opt, _ = st.columns([1, 2])
    with col_tab_opt:
        table_view = st.radio(
            "Display Format:",
            ["Full-Text Readable Table", "Interactive Grid"],
            horizontal=True,
            label_visibility="collapsed"
        )
        
    if table_view == "Full-Text Readable Table":
        st.table(skills_data)
    else:
        st.dataframe(
            skills_data,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Domain": st.column_config.TextColumn("Domain", width="small"),
                "Skill / Technology": st.column_config.TextColumn("Skill / Technology", width="medium"),
                "Real-World Application / Project": st.column_config.TextColumn("Real-World Application / Project", width="large"),
            }
        )

# =============================================================================
# TAB 3: PROJECT PORTFOLIO
# =============================================================================
with tab_projects:
    st.header("Project Portfolio: Ranked Engineering & Research Systems")
    st.write(
        "A curated collection of machine learning systems, assistive healthcare tools, and full-stack applications. "
        "Each project is documented with my specific role, technologies, and technical outcomes."
    )
    
    # Category Filter
    col_filter_1, col_filter_2 = st.columns([1, 2])
    with col_filter_1:
        cat_options = ["All Categories"] + sorted(list(set(p["category"] for p in projects_list)))
        selected_category = st.selectbox("Filter by Category:", options=cat_options, index=0)
    with col_filter_2:
        all_tools = sorted(list(set(tool for p in projects_list for tool in p["tools"])))
        selected_tools = st.multiselect("Filter by Technology Stack:", options=all_tools, default=[])

    display_projects = projects_list
    if selected_category != "All Categories":
        display_projects = [p for p in display_projects if p["category"] == selected_category]
    if selected_tools:
        display_projects = [p for p in display_projects if any(tool in p["tools"] for tool in selected_tools)]
    if sidebar_domain_filter == "Machine Learning & AI":
        display_projects = [p for p in display_projects if p["category"] == "Machine Learning & AI"]
    elif sidebar_domain_filter == "Community & Social Impact":
        display_projects = [p for p in display_projects if p["category"] == "Assistive & Community" or "PSC" in p.get("accolade", "")]

    st.markdown(f"*Showing **{len(display_projects)}** documented systems:*")
    st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)
    
    def render_project_card(p):
        tools_html = ' '.join([f'<span class="tag-pill">{t}</span>' for t in p['tools']])
        metrics_html = ''.join([
            f'<div class="metric-row"><span class="metric-key">{k}:</span><span class="metric-val">{v}</span></div>'
            for k, v in p["metrics"].items()
        ])
        
        return f"""
        <div class="botanical-card">
            <div class="card-content-body">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <span class="tag-accent">Rank {p['rank']}</span>
                    <span class="tag-pill" style="margin-right: 0;">{p['category']}</span>
                </div>
                <h3 class="card-title">{p['title']}</h3>
                <div class="card-accolade">
                    {p['accolade']}
                </div>
                <div class="card-role">
                    <strong>Role:</strong> {p['role']}
                </div>
                <p class="card-summary">{p['summary']}</p>
                <div class="card-tools">
                    {tools_html}
                </div>
            </div>
            <div class="card-content-footer">
                <div class="card-link-wrapper">
                    <a href="{p['repo']}" target="_blank" class="card-repo-link">
                        Explore Repository & Documentation &rarr;
                    </a>
                </div>
                <details class="apple-details">
                    <summary class="apple-summary">
                        <span>Technical Architecture: {p['title'].split('—')[0].strip()}</span>
                        <span class="apple-chevron">›</span>
                    </summary>
                    <div class="apple-details-content">
                        {metrics_html}
                    </div>
                </details>
            </div>
        </div>
        """
    
    for idx in range(0, len(display_projects), 2):
        col_p1, col_p2 = st.columns(2)
        with col_p1:
            st.markdown(render_project_card(display_projects[idx]), unsafe_allow_html=True)
        if idx + 1 < len(display_projects):
            with col_p2:
                st.markdown(render_project_card(display_projects[idx + 1]), unsafe_allow_html=True)

# =============================================================================
# TAB 4: DISPATCH & INQUIRIES
# =============================================================================
with tab_dispatch:
    st.header("Dispatch Terminal: Send a Message or Collaboration Inquiry")
    st.write(
        "Have an idea for a machine learning collaboration, community application, or research inquiry? "
        "Leave a note below."
    )
    
    col_form, col_log = st.columns([3, 2])
    
    with col_form:
        with st.form("carrier_dispatch_form", clear_on_submit=True):
            st.subheader("Dispatch a Message")
            
            c_name = st.text_input("Your Full Name:", placeholder="e.g. Maria Santos")
            c_email = st.text_input("Your Email Address:", placeholder="e.g. maria@example.com")
            c_inquiry = st.selectbox(
                "Purpose of Contact:",
                options=[
                    "Applied Machine Learning Collaboration",
                    "Community & Social Impact Initiative",
                    "Academic Mentorship / Research Inquiry",
                    "General Friendly Greeting"
                ]
            )
            c_message = st.text_area("Your Message:", placeholder="Share your thoughts, opportunity, or feedback...", height=130)
            c_receipt = st.checkbox("Request return dispatch confirmation receipt", value=True)
            
            submitted = st.form_submit_button("Send Dispatch", use_container_width=True)
            
            if submitted:
                if not c_name.strip() or not c_message.strip():
                    st.error("Please provide both your name and a message before submitting.")
                else:
                    new_entry = {
                        "sender": c_name.strip(),
                        "type": c_inquiry,
                        "message": c_message.strip(),
                        "date": "Just now"
                    }
                    st.session_state["guestbook"].append(new_entry)
                    st.success(f"Dispatch sent successfully. Thank you, {c_name}.")
                    st.toast("Message received.")

    with col_log:
        st.subheader("Recent Inquiries")
        
        for item in reversed(st.session_state["guestbook"]):
            st.markdown(f"""
            <div class="botanical-card" style="padding: 12px 16px; margin-bottom: 10px;">
                <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 0.8rem; font-weight: 600; color: var(--heading-color);">
                    {item['sender']} &nbsp;·&nbsp; <span style="color: var(--accent-color);">{item['type']}</span>
                </div>
                <div style="font-size: 0.9rem; margin-top: 4px; color: var(--text-primary);">
                    "{item['message']}"
                </div>
                <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 0.72rem; color: var(--text-muted); margin-top: 6px;">
                    Logged: {item['date']}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
        st.markdown("---")
        st.markdown("""
        **Direct Communication Lines:**  
        Location: Cebu City, Philippines  
        Email: `cruzgian008@gmail.com`  
        Phone: `(+63) 915 026 2014`  
        GitHub: [github.com/Gianne818](https://github.com/Gianne818)
        """)

# -----------------------------------------------------------------------------
# 9. Footer
# -----------------------------------------------------------------------------
st.markdown("---")
col_foot_1, col_foot_2 = st.columns([3, 1])
with col_foot_1:
    st.markdown(
        "<small style='color: var(--text-muted);'>Charlone Gianne V. Cruz · 3rd Year BSCS · Cebu Institute of Technology – University · CSIT 349 (Applied AI)</small>",
        unsafe_allow_html=True
    )
with col_foot_2:
    st.markdown(
        "<small style='color: var(--text-muted); float: right;'>Naturalist Field Guide Edition</small>",
        unsafe_allow_html=True
    )
