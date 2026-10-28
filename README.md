# Charlone Gianne V. Cruz — Autobiography & Portfolio
**CSIT 349 · Applied AI** | Cebu Institute of Technology – University (CIT-U)  
*3rd Year Bachelor of Science in Computer Science (BSCS)*  

An editorial, bird- and botanical-themed portfolio built with **Streamlit**, featuring clean humanist typography, interactive data visualizations, and full technical documentation of ranked machine learning, biomedical AI, and full-stack projects.

---

## 🚀 Quickstart & Local Execution

Ensure you are in the project folder and run with your Python environment:

```bash
# Using the virtual environment
.venv/bin/streamlit run app.py

# Or with global/active environment
streamlit run app.py
```

---

## 📋 Rubric & Component Coverage (100 pts + 10 pts Bonus)

| Rubric Criterion | Target | Implementation Details |
| :--- | :---: | :--- |
| **Content (40 pts)** | Autobiography + ≥3 Projects | Features detailed autobiography (education, CIT-U background, passions for music, birds, plants, and tech for a cause), plus all **10 ranked projects** with PAROLA (PSC Top 25 Finalist), PhysioCGM Hypoglycemia research, and IMentia prominently documented. |
| **Components (35 pts)** | Lecture Set + ≥4 Extras | **Core**: `st.title`, `st.header`, `st.write`, `st.markdown`, `st.dataframe`, `st.altair_chart`, `st.button`, `st.slider`, `st.selectbox`, `st.checkbox`, `st.text_input`, `st.text_area`, `st.radio`, `st.multiselect`, `st.sidebar`, `st.columns`.<br>**Extras**: `st.image` (botanical SVG avatar & photo uploader), `st.tabs` (4 chapters), `st.metric` (flight hours & projects), `st.form` (carrier dispatch), `st.session_state` (live guestbook), `st.download_button` (dossier export), `st.expander` (technical architectures), `st.toast` and `st.balloons()`. |
| **Design (25 pts)** | Clear layout, easy scanning | Warm botanical palette (`#FAF7F2`, `#1B3B2B`, `#C27D38`), Google Font `Newsreader` + `Plus Jakarta Sans`, quiet card borders, anti-slop principles. |
| **Bonus (+10 pts)** | Streamlit Community Cloud | Self-contained, lightweight `requirements.txt` (`streamlit`, `pandas`, `altair`), zero secret leaks, ready for public GitHub push and 1-click deployment on `share.streamlit.io`. |

---

## ☁️ Deployment Guide (Streamlit Community Cloud Bonus)

1. Create a public repository on GitHub (e.g. `Streamlit-Portfolio`).
2. Push `app.py`, `requirements.txt`, `assets/`, and `README.md`.
3. Sign in to [share.streamlit.io](https://share.streamlit.io).
4. Select your repo and branch, set main file path to `app.py`, and click **Deploy**.
5. Submit the public `.streamlit.app` link for the +10 bonus points!
