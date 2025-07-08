import streamlit as st

categories = ["Spoken English", "Spoken Hindi", "Abacus", "Typing", "Computer", "Tailoring", "Dance"]

learning_centers = {
    "Spoken English": [
        {"name": "Saraswathi Spoken English", "address": "Main Rd, Komarapalayam", "rating": 4.7, "detail": "Grammar, Vocabulary, and Communication"},
        {"name": "Vijay English Academy", "address": "Near Bus Stand, Komarapalayam", "rating": 4.5, "detail": "Spoken English with practice sessions"},
    ],
    "Spoken Hindi": [
        {"name": "Friends Hindi Class", "address": "South Street, Komarapalayam", "rating": 4.6, "detail": "Basic to Advanced Hindi"},
        {"name": "Ravi’s Hindi Tuition", "address": "4th Cross, Namakkal", "rating": 4.4, "detail": "Speaking and writing Hindi"},
    ],
    "Abacus": [
        {"name": "Golden Beads Abacus", "address": "MG Road, Komarapalayam", "rating": 4.8, "detail": "Mental math and speed calculation"},
        {"name": "Kids Brain Abacus", "address": "School St, Komarapalayam", "rating": 4.5, "detail": "Junior and Senior abacus levels"},
    ],
    "Typing": [
        {"name": "Brilliant Typewriting", "address": "Anangur Rd, Komarapalayam", "rating": 4.8, "detail": "Tamil & English typing"},
        {"name": "Rasi Type Institute", "address": "Old Bus Stand, Komarapalayam", "rating": 4.6, "detail": "Govt typing exam focused"},
    ],
    "Computer": [
        {"name": "CSC Computer Education", "address": "Market Rd, Komarapalayam", "rating": 4.7, "detail": "Basic, Tally, DTP, C, C++"},
        {"name": "Apollo Computer", "address": "New Colony, Komarapalayam", "rating": 4.6, "detail": "MS Office, Web Design"},
    ],
    "Tailoring": [
        {"name": "Agam Tailoring Institute", "address": "Komarapalayam Main Rd", "rating": 4.9, "detail": "Blouse, Chudidar, Aari work"},
        {"name": "Selvi Tailoring", "address": "East Street, Namakkal", "rating": 4.5, "detail": "Women’s tailoring with kit"},
    ],
    "Dance": [
        {"name": "Senz X Dance Studio", "address": "Komarapalayam Bus Stand", "rating": 4.8, "detail": "Western & Classical dance"},
        {"name": "Pranava Dance School", "address": "Near Govt School, Komarapalayam", "rating": 4.7, "detail": "Bharatanatyam, Cinematic"},
    ]
}

st.title("📚 Affordable Learning Centers")
st.write("Select a category to see classes:")

category = st.selectbox("Choose a Category", categories)

if category:
    centers = learning_centers.get(category, [])
    for center in centers:
        st.markdown(f"🏫 **{center['name']}**")
        st.markdown(f"📍 Address: {center['address']}")
        st.markdown(f"⭐ Rating: {center['rating']}")
        st.markdown(f"📝 {center['detail']}")
        st.markdown("---")




