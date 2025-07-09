import streamlit as st import pandas as pd

---------------------- Data ----------------------

data = [ # Spoken English & Hindi {"name": "Flora Academy", "category": "Spoken Hindi", "location": "Komarapalayam", "rating": 5.0, "details": "They teach Hindi in a better, simple-to-understand way.", "icon": "🗣️"},

{"name": "Vinayak Spoken Hindi", "category": "Spoken Hindi", "location": "Komarapalayam", "rating": 4.9,
 "details": "Great for learning spoken Hindi. Also teaches spoken English.",
 "icon": "🗣️"},

{"name": "Pioneer Academy", "category": "Spoken English", "location": "Komarapalayam", "rating": 4.9,
 "details": "Teaches English, Hindi, abacus, TNPSC, typing, tailoring, silambam.",
 "icon": "🗣️"},

{"name": "Kathirvel Hindi Tuition", "category": "Spoken Hindi", "location": "Komarapalayam", "rating": None,
 "details": "Offers Hindi tuition. Also teaches spoken English.",
 "icon": "🗣️"},

# Abacus
{"name": "Indian Abacus Centre", "category": "Abacus", "location": "Erode", "rating": 4.9,
 "details": "Handwriting, calligraphy, spoken Tamil/English.",
 "icon": "🧮"},

{"name": "SIP Abacus", "category": "Abacus", "location": "Erode", "rating": 4.9,
 "details": "Well-known abacus center.",
 "icon": "🧮"},

{"name": "Agam Academy", "category": "Abacus", "location": "Erode", "rating": 4.9,
 "details": "Abacus and skill development.",
 "icon": "🧮"},

{"name": "Golden Buds Abacus Academy", "category": "Abacus", "location": "Erode", "rating": 5.0,
 "details": "Mental math training.",
 "icon": "🧮"},

# Typewriting
{"name": "Brilliant Typewriting Class", "category": "Typing", "location": "Komarapalayam", "rating": None,
 "details": "Typewriting classes.", "icon": "🔠"},

# Computer
{"name": "CSC Computer Education", "category": "Computer", "location": "Komarapalayam", "rating": 4.8,
 "details": "Computer basics, MS Office, Internet.", "icon": "💻"},

{"name": "IFC Infotech", "category": "Computer", "location": "Komarapalayam", "rating": 5.0,
 "details": "Hardware, software, multimedia.", "icon": "💻"},

# Tailoring
{"name": "Anubi Designing Institute", "category": "Tailoring", "location": "Komarapalayam", "rating": 5.0,
 "details": "Designing & tailoring training.", "icon": "🧵"},

{"name": "Janani Designers", "category": "Tailoring", "location": "Komarapalayam", "rating": 4.8,
 "details": "Tailoring services.", "icon": "🧵"},

# Dance
{"name": "Senz X Dance Class", "category": "Dance", "location": "Komarapalayam", "rating": 4.8,
 "details": "Dance classes for all ages.", "icon": "💃"},

{"name": "Maaran Dance Studio", "category": "Dance", "location": "Komarapalayam", "rating": 5.0,
 "details": "Professional dance studio.", "icon": "💃"},

{"name": "Dance Dreamers", "category": "Dance", "location": "Komarapalayam", "rating": 5.0,
 "details": "Creative dance space.", "icon": "💃"},

]

---------------------- App ----------------------

st.set_page_config(page_title="Affordable Learning Centers", layout="centered") st.title("📚 Affordable Learning & Training Centers")

Convert to DataFrame

df = pd.DataFrame(data)

---------------------- Filters ----------------------

categories = sorted(df["category"].unique()) locations = sorted(df["location"].unique())

col1, col2, col3 = st.columns([2, 2, 2])

with col1: selected_category = st.selectbox("📘 Select Category", ["All"] + categories)

with col2: selected_location = st.selectbox("📍 Select Location", ["All"] + locations)

with col3: sort_option = st.selectbox("🔽 Sort by Rating", ["Default", "Highest to Lowest"])

search_term = st.text_input("🔎 Search by Center Name")

---------------------- Filter Logic ----------------------

filtered = df.copy()

if selected_category != "All": filtered = filtered[filtered["category"] == selected_category] if selected_location != "All": filtered = filtered[filtered["location"] == selected_location] if search_term: filtered = filtered[filtered["name"].str.contains(search_term, case=False)] if sort_option == "Highest to Lowest": filtered = filtered.sort_values(by="rating", ascending=False, na_position='last')

st.markdown(f"### 🎯 {len(filtered)} centers found")

---------------------- Display Cards ----------------------

for _, row in filtered.iterrows(): with st.container(): st.markdown(f"#### {row['icon']} {row['name']}") st.markdown(f"📍 {row['location']}") if row["rating"]: st.markdown(f"⭐ {row['rating']}") st.markdown(f"📝 {row['details']}") st.markdown("---")

---------------------- Footer ----------------------

st.markdown("\n") st.markdown("<center><sub>Built with ❤️ by Dhaniya Sri using Streamlit</sub></center>", unsafe_allow_html=True)







