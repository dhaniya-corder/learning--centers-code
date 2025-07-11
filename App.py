import streamlit as st

--- Data ---

categories = [ "Spoken English", "Spoken Hindi", "Abacus", "Typing", "Computer", "Tailoring", "Dance" ]

learning_centers = { "Spoken English": [ {"name": "Flora Academy", "address": "Komarapalayam", "rating": 5.0, "desc": "இங்கே இந்தி மொழியை எளிதாக கற்றுக்கொள்ளலாம்."}, {"name": "Vinayak Spoken Hindi", "address": "Komarapalayam", "rating": 4.9, "desc": "இந்தி மற்றும் ஆங்கிலம் பேச கற்பிக்கின்றனர்."}, {"name": "Pioneer Academy", "address": "Komarapalayam", "rating": 4.9, "desc": "Spoken English, Hindi, abacus, typing, tailoring, silambam போன்றவை கற்பிக்கின்றனர்."}, {"name": "Kathirvel Hindi Tuition", "address": "Komarapalayam", "rating": "N/A", "desc": "இந்தி மற்றும் ஆங்கிலம் பேச கற்பிக்கின்றனர்."}, ], "Spoken Hindi": [ {"name": "Flora Academy", "address": "Komarapalayam", "rating": 5.0, "desc": "இங்கே இந்தி மொழியை எளிதாக கற்றுக்கொள்ளலாம்."}, {"name": "Vinayak Spoken Hindi", "address": "Komarapalayam", "rating": 4.9, "desc": "இந்தி மற்றும் ஆங்கிலம் பேச கற்பிக்கின்றனர்."}, {"name": "Pioneer Academy", "address": "Komarapalayam", "rating": 4.9, "desc": "Spoken English, Hindi, abacus, typing, tailoring, silambam போன்றவை கற்பிக்கின்றனர்."}, {"name": "Kathirvel Hindi Tuition", "address": "Komarapalayam", "rating": "N/A", "desc": "இந்தி மற்றும் ஆங்கிலம் பேச கற்பிக்கின்றனர்."}, ], "Abacus": [ {"name": "Pioneer Academy", "address": "Komarapalayam", "rating": 4.9, "desc": "Abacus, tailoring, typing, spoken English/Hindi ஆகியவை கற்பிக்கின்றனர்."}, {"name": "Indian Abacus Centre", "address": "Erode", "rating": 4.9, "desc": "Handwriting, spoken Tamil, spoken English ஆகியவை கூட சேர்த்து கற்பிக்கின்றனர்."}, {"name": "SIP Abacus", "address": "Erode", "rating": 4.9, "desc": "அபாக்கஸ் பயிற்சி"}, {"name": "Agam Academy", "address": "Erode", "rating": 4.9, "desc": "Skill development classes உடன் abacus பயிற்சி"}, {"name": "Golden Buds Abacus Academy", "address": "Erode", "rating": 5.0, "desc": "மனித மெமரி மேம்பாட்டிற்கான பயிற்சி"}, ], "Typing": [ {"name": "Brilliant Typewriting Class", "address": "Komarapalayam", "rating": "N/A", "desc": "தமிழ் & ஆங்கில டைப்பிங்"}, {"name": "Pioneer Academy", "address": "Komarapalayam", "rating": 4.9, "desc": "Typing உடன் spoken & tailoring கற்றுத்தரப்படுகின்றது"}, ], "Computer": [ {"name": "CSC Computer Education", "address": "Komarapalayam", "rating": 4.8, "desc": "MS Office, internet, basics பயிற்சி"}, {"name": "IFC Infotech", "address": "Komarapalayam", "rating": 5.0, "desc": "Hardware, software, multimedia போன்றவை கற்பிக்கின்றனர்"}, {"name": "Pioneer Academy", "address": "Komarapalayam", "rating": 4.9, "desc": "Computer, typing, tailoring போன்றவை கற்பிக்கின்றனர்"}, ], "Tailoring": [ {"name": "Anubi Designing Institute", "address": "Komarapalayam", "rating": 5.0, "desc": "Tailoring மற்றும் Design பயிற்சி"}, {"name": "Aparnaa Costume Designer", "address": "Erode", "rating": 4.9, "desc": "Tailoring மற்றும் Costume design"}, {"name": "Apurvaa Fashion Institute", "address": "Erode", "rating": 5.0, "desc": "Tailoring மற்றும் Beautician"}, {"name": "Janani Designers", "address": "Komarapalayam", "rating": 4.8, "desc": "Tailoring பயிற்சி"}, {"name": "BE Relax Tailoring", "address": "Bhavani", "rating": 4.5, "desc": "Tailoring பயிற்சி"}, {"name": "Agni Poo Tailoring Institute", "address": "Bhavani", "rating": 5.0, "desc": "Tailoring பயிற்சி"}, {"name": "Aarah Aari Institute", "address": "Bhavani", "rating": 5.0, "desc": "Aari work & tailoring"}, ], "Dance": [ {"name": "Senz X Dance Class", "address": "Komarapalayam", "rating": 4.8, "desc": "Dance for kids and adults"}, {"name": "Maaran Dance Studio", "address": "Komarapalayam", "rating": 5.0, "desc": "Dance class with practice stage"}, {"name": "Dance Dreamers", "address": "Komarapalayam", "rating": 5.0, "desc": "Dance training for all age groups"}, ] }

--- UI ---

st.title("📚 மலிவு தரமான கற்றல் நிலையங்கள்") st.write("வகையைத் தேர்ந்தெடுத்து இடங்களை பாருங்கள்:")

category = st.selectbox("வகை தேர்வு செய்யவும்", categories) search_query = st.text_input("🔍 பெயர் அல்லது விளக்கம் மூலம் தேடுங்கள்") location_filter = st.text_input("📍 இடம் (எ.கா., Komarapalayam)")

if category: results = learning_centers.get(category, [])

# Apply search and location filter
if search_query:
    results = [c for c in results if search_query.lower() in c["name"].lower() or search_query.lower() in c["desc"].lower()]
if location_filter:
    results = [c for c in results if location_filter.lower() in c["address"].lower()]

for center in results:
    st.subheader(f"🏫 {center['name']}")
    st.write(f"📍 முகவரி: {center['address']}")
    st.write(f"⭐ மதிப்பீடு: {center['rating']}")
    st.write(f"📝 விவரம்: {center['desc']}")

else: st.warning("முதலில் ஒரு வகையை தேர்ந்தெடுக்கவும்.")

import streamlit as st

--- Data ---

categories = [ "Spoken English", "Spoken Hindi", "Abacus", "Typing", "Computer", "Tailoring", "Dance" ]

learning_centers = { "Spoken English": [ {"name": "Flora Academy", "address": "Komarapalayam", "rating": 5.0, "desc": "இங்கே இந்தி மொழியை எளிதாக கற்றுக்கொள்ளலாம்."}, {"name": "Vinayak Spoken Hindi", "address": "Komarapalayam", "rating": 4.9, "desc": "இந்தி மற்றும் ஆங்கிலம் பேச கற்பிக்கின்றனர்."}, {"name": "Pioneer Academy", "address": "Komarapalayam", "rating": 4.9, "desc": "Spoken English, Hindi, abacus, typing, tailoring, silambam போன்றவை கற்பிக்கின்றனர்."}, {"name": "Kathirvel Hindi Tuition", "address": "Komarapalayam", "rating": "N/A", "desc": "இந்தி மற்றும் ஆங்கிலம் பேச கற்பிக்கின்றனர்."}, ], "Spoken Hindi": [ {"name": "Flora Academy", "address": "Komarapalayam", "rating": 5.0, "desc": "இங்கே இந்தி மொழியை எளிதாக கற்றுக்கொள்ளலாம்."}, {"name": "Vinayak Spoken Hindi", "address": "Komarapalayam", "rating": 4.9, "desc": "இந்தி மற்றும் ஆங்கிலம் பேச கற்பிக்கின்றனர்."}, {"name": "Pioneer Academy", "address": "Komarapalayam", "rating": 4.9, "desc": "Spoken English, Hindi, abacus, typing, tailoring, silambam போன்றவை கற்பிக்கின்றனர்."}, {"name": "Kathirvel Hindi Tuition", "address": "Komarapalayam", "rating": "N/A", "desc": "இந்தி மற்றும் ஆங்கிலம் பேச கற்பிக்கின்றனர்."}, ], "Abacus": [ {"name": "Pioneer Academy", "address": "Komarapalayam", "rating": 4.9, "desc": "Abacus, tailoring, typing, spoken English/Hindi ஆகியவை கற்பிக்கின்றனர்."}, {"name": "Indian Abacus Centre", "address": "Erode", "rating": 4.9, "desc": "Handwriting, spoken Tamil, spoken English ஆகியவை கூட சேர்த்து கற்பிக்கின்றனர்."}, {"name": "SIP Abacus", "address": "Erode", "rating": 4.9, "desc": "அபாக்கஸ் பயிற்சி"}, {"name": "Agam Academy", "address": "Erode", "rating": 4.9, "desc": "Skill development classes உடன் abacus பயிற்சி"}, {"name": "Golden Buds Abacus Academy", "address": "Erode", "rating": 5.0, "desc": "மனித மெமரி மேம்பாட்டிற்கான பயிற்சி"}, ], "Typing": [ {"name": "Brilliant Typewriting Class", "address": "Komarapalayam", "rating": "N/A", "desc": "தமிழ் & ஆங்கில டைப்பிங்"}, {"name": "Pioneer Academy", "address": "Komarapalayam", "rating": 4.9, "desc": "Typing உடன் spoken & tailoring கற்றுத்தரப்படுகின்றது"}, ], "Computer": [ {"name": "CSC Computer Education", "address": "Komarapalayam", "rating": 4.8, "desc": "MS Office, internet, basics பயிற்சி"}, {"name": "IFC Infotech", "address": "Komarapalayam", "rating": 5.0, "desc": "Hardware, software, multimedia போன்றவை கற்பிக்கின்றனர்"}, {"name": "Pioneer Academy", "address": "Komarapalayam", "rating": 4.9, "desc": "Computer, typing, tailoring போன்றவை கற்பிக்கின்றனர்"}, ], "Tailoring": [ {"name": "Anubi Designing Institute", "address": "Komarapalayam", "rating": 5.0, "desc": "Tailoring மற்றும் Design பயிற்சி"}, {"name": "Aparnaa Costume Designer", "address": "Erode", "rating": 4.9, "desc": "Tailoring மற்றும் Costume design"}, {"name": "Apurvaa Fashion Institute", "address": "Erode", "rating": 5.0, "desc": "Tailoring மற்றும் Beautician"}, {"name": "Janani Designers", "address": "Komarapalayam", "rating": 4.8, "desc": "Tailoring பயிற்சி"}, {"name": "BE Relax Tailoring", "address": "Bhavani", "rating": 4.5, "desc": "Tailoring பயிற்சி"}, {"name": "Agni Poo Tailoring Institute", "address": "Bhavani", "rating": 5.0, "desc": "Tailoring பயிற்சி"}, {"name": "Aarah Aari Institute", "address": "Bhavani", "rating": 5.0, "desc": "Aari work & tailoring"}, ], "Dance": [ {"name": "Senz X Dance Class", "address": "Komarapalayam", "rating": 4.8, "desc": "Dance for kids and adults"}, {"name": "Maaran Dance Studio", "address": "Komarapalayam", "rating": 5.0, "desc": "Dance class with practice stage"}, {"name": "Dance Dreamers", "address": "Komarapalayam", "rating": 5.0, "desc": "Dance training for all age groups"}, ] }

--- UI ---

st.title("📚 மலிவு தரமான கற்றல் நிலையங்கள்") st.write("வகையைத் தேர்ந்தெடுத்து இடங்களை பாருங்கள்:")

category = st.selectbox("வகை தேர்வு செய்யவும்", categories) search_query = st.text_input("🔍 பெயர் அல்லது விளக்கம் மூலம் தேடுங்கள்") location_filter = st.text_input("📍 இடம் (எ.கா., Komarapalayam)")

if category: results = learning_centers.get(category, [])

# Apply search and location filter
if search_query:
    results = [c for c in results if search_query.lower() in c["name"].lower() or search_query.lower() in c["desc"].lower()]
if location_filter:
    results = [c for c in results if location_filter.lower() in c["address"].lower()]

for center in results:
    st.subheader(f"🏫 {center['name']}")
    st.write(f"📍 முகவரி: {center['address']}")
    st.write(f"⭐ மதிப்பீடு: {center['rating']}")
    st.write(f"📝 விவரம்: {center['desc']}")

else: st.warning("முதலில் ஒரு வகையை தேர்ந்தெடுக்கவும்.")









