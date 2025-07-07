import streamlit as st

st.set_page_config(page_title="Learning Centers", layout="centered")

st.title("📚 Affordable Learning Centers in Tamil Nadu")
st.markdown("Browse and explore classes near you. Search, filter, and explore by category.")

# --- Data ---
categories = [
    "Spoken English", "Spoken Hindi", "Abacus",
    "Typing", "Computer", "Tailoring", "Dance"
]

learning_centers = {
    "Spoken English": [
        {"name": "Pioneer Academy", "address": "Komarapalayam, Tamil Nadu", "rating": 4.9, "detail": "Teaches English, Hindi, typing, computer."},
        {"name": "Vinayak Spoken English", "address": "Komarapalayam, Tamil Nadu", "rating": 4.9, "detail": "Training for English communication."}
    ],
    "Spoken Hindi": [
        {"name": "Flora Academy", "address": "1st Floor, SK Dental Hospital Complex, Komarapalayam", "rating": 5.0, "detail": "They teach Hindi in a better way."},
        {"name": "Vinayak Spoken Hindi", "address": "Komarapalayam, Tamil Nadu", "rating": 4.9, "detail": "Great for learning spoken Hindi."},
        {"name": "Pioneer Academy", "address": "Komarapalayam, Tamil Nadu", "rating": 4.9, "detail": "Also offers Spoken Hindi."},
        {"name": "Kathirvel Hindi Tuition", "address": "Near Sriram Maligai Store, West Colony, Vijayathottam, Komarapalayam", "rating": None, "detail": "Spoken Hindi tuition."}
    ],
    "Abacus": [
        {"name": "Pioneer Academy", "address": "Komarapalayam, Tamil Nadu", "rating": 4.9, "detail": "Abacus, TNPSC, silambam, tailoring, typing, computer classes."},
        {"name": "Indian Abacus Centre", "address": "Karungalpalayam, Erode", "rating": 4.9, "detail": "Offers handwriting, calligraphy, spoken Tamil and English."},
        {"name": "SIP Abacus", "address": "Gandhiji Street, Kollampalayam, Erode", "rating": 4.9, "detail": "Abacus training for kids."},
        {"name": "Agam Academy", "address": "Vellusamy Street, Manickampalayam, Erode", "rating": 4.9, "detail": "Abacus and tailoring classes."},
        {"name": "Golden Buds Abacus Academy", "address": "149/320, Valayakara Street, Erode", "rating": 5.0, "detail": "Expert abacus coaching."}
    ],
    "Typing": [
        {"name": "Brilliant Typewriting", "address": "284F, Anangur Road, Opp. Salem Main Road, Komarapalayam", "rating": 4.8, "detail": "English & Tamil typing."},
        {"name": "Pioneer Academy", "address": "Komarapalayam, Tamil Nadu", "rating": 4.9, "detail": "Typing and other skill classes."}
    ],
    "Computer": [
        {"name": "CSC Computer Education", "address": "Vasavi Complex, Nadraja Nagar, Komarapalayam", "rating": 4.8, "detail": "Computer basics to advanced."},
        {"name": "IFC Infotech Computer Education", "address": "Bus Stand, T.R. Complex, Salem Main Road, Komarapalayam", "rating": 5.0, "detail": "Great for software training."},
        {"name": "Pioneer Academy", "address": "Komarapalayam, Tamil Nadu", "rating": 4.9, "detail": "Includes computer classes."}
    ],
    "Tailoring": [
        {"name": "Agam Academy", "address": "Vellusamy Street, Manickampalayam, Erode", "rating": 4.9, "detail": "Tailoring classes with abacus."},
        {"name": "Pioneer Academy", "address": "Komarapalayam, Tamil Nadu", "rating": 4.9, "detail": "Offers tailoring as one of its courses."}
    ],
    "Dance": [
        {"name": "Senz X Dance Class", "address": "Pallipalayam-Komarapalayam Road, Apex Colony, Komarapalayam", "rating": 4.8, "detail": "Modern & creative dance training."},
        {"name": "Maaran Dance Studio", "address": "Salem Main Road, Opp. State Bank of India, Komarapalayam", "rating": 5.0, "detail": "Professional dance coaching."},
        {"name": "Dance Dreamers", "address": "Opp. Salem Main Road, 294/5, Kongu Finance Upstairs, Near Saravana Theatre, Komarapalayam", "rating": 5.0, "detail": "Energetic youth dance club."}
    ]
}

# --- Filters ---
col1, col2 = st.columns(2)
with col1:
    selected_category = st.selectbox("🎯 Choose a category", categories)
with col2:
    search_text = st.text_input("🔍 Search by name or address").strip().lower()

# --- Display Centers ---
if selected_category:
    results = []
    for center in learning_centers[selected_category]:
        if search_text in center['name'].lower() or search_text in center['address'].lower():
            results.append(center)

    if results:
        for center in results:
            st.markdown(f"### 🏫 {center['name']}")
            st.write(f"📍 Address: {center['address']}")
            st.write(f"⭐ Rating: {center['rating'] if center['rating'] else 'Not rated'}")
            st.write(f"📝 {center['detail']}")
            st.markdown("---")
    else:
        st.info("No results found. Try changing your search.")




