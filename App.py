import streamlit as st

categories = ["Spoken English", "Spoken Hindi", "Abacus", "Typing", "Computer", "Tailoring", "Dance"]

learning_centers = {
    "Spoken English": [{"name": "Pioneer Academy", "address": "Komarapalayam", "rating": "4.9", "detail": "Teaches English, Hindi, typing, etc."}],
    "Spoken Hindi": [{"name": "Flora Academy", "address": "SK Dental Complex, Komarapalayam", "rating": "5.0", "detail": "Best for Hindi spoken"}],
    "Abacus": [{"name": "Golden Buds", "address": "Valayakara St, Erode", "rating": "5.0", "detail": "Strong abacus foundation"}],
    "Typing": [{"name": "Brilliant Typewriting", "address": "Anangur Rd, Komarapalayam", "rating": "4.8", "detail": "Tamil & English typing"}],
    "Computer": [{"name": "CSC Computer", "address": "Vasavi Complex, Komarapalayam", "rating": "4.8", "detail": "Computer basics to advanced"}],
    "Tailoring": [{"name": "Agam Academy", "address": "Manickam Palayam, Erode", "rating": "4.9", "detail": "Tailoring & crafts"}],
    "Dance": [{"name": "Senz X Dance", "address": "Apex Colony, Komarapalayam", "rating": "4.8", "detail": "Fun energetic dance"}]
}

st.title("📚 Affordable Learning Centers")
st.write("Select a category to see classes:")

category = st.selectbox("Choose a Category", categories)

if category:
    centers = learning_centers.get(category, [])
    for c in centers:
        st.subheader(f"🏫 {c['name']}")
        st.write(f"📍 Address: {c['address']}")
        st.write(f"⭐ Rating: {c['rating']}")
        st.write(f"📝 {c['detail']}")
        st.write("---")
