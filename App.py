import streamlit as st

st.title("📚 Affordable Learning Centers")
st.write("Select a category and location to see classes:")

# Filter options
categories = [
    "Spoken English & Hindi", "Abacus", "Typing",
    "Computer", "Tailoring", "Dance"
]
locations = [
    "Komarapalayam", "Erode", "Bhavani"
]

# Select filters
selected_category = st.selectbox("Choose a Category", categories)
selected_location = st.selectbox("Choose a Location", locations)

# All centers data
learning_centers = {
    "Spoken English & Hindi": [
        {
            "name": "Flora Academy",
            "address": "1st Floor, Pallipalayam Corner, Komarapalayam",
            "rating": "5.0",
            "details": "Teaches Hindi simply and effectively.",
            "location": "Komarapalayam"
        },
        {
            "name": "Vinayak Spoken Hindi",
            "address": "Komarapalayam",
            "rating": "4.9",
            "details": "Teaches Hindi and English.",
            "location": "Komarapalayam"
        },
        {
            "name": "Pioneer Academy",
            "address": "Santhapuri Nagar, Komarapalayam",
            "rating": "4.9",
            "details": "Teaches multiple subjects.",
            "location": "Komarapalayam"
        },
        {
            "name": "Kathirvel Hindi Tuition",
            "address": "West Colony, Komarapalayam",
            "rating": "Not available",
            "details": "Offers spoken Hindi and English.",
            "location": "Komarapalayam"
        }
    ],
    "Abacus": [
        {
            "name": "Pioneer Academy",
            "address": "Santhapuri Nagar, Komarapalayam",
            "rating": "4.9",
            "details": "Abacus and more.",
            "location": "Komarapalayam"
        },
        {
            "name": "Indian Abacus Centre",
            "address": "Karungalpalayam, Erode",
            "rating": "4.9",
            "details": "Also teaches handwriting.",
            "location": "Erode"
        },
        {
            "name": "SIP Abacus",
            "address": "Gandhiji Street, Erode",
            "rating": "4.9",
            "details": "Well-known abacus center.",
            "location": "Erode"
        },
        {
            "name": "Agam Academy",
            "address": "Manickampalayam, Erode",
            "rating": "4.9",
            "details": "Abacus and skill classes.",
            "location": "Erode"
        },
        {
            "name": "Golden Buds Abacus Academy",
            "address": "Valayakara Street, Erode",
            "rating": "5.0",
            "details": "Focused on mental math.",
            "location": "Erode"
        }
    ],
    "Typing": [
        {
            "name": "Brilliant Typewriting Class",
            "address": "Anangur Rd, Komarapalayam",
            "rating": "Not available",
            "details": "Tamil & English typing.",
            "location": "Komarapalayam"
        },
        {
            "name": "Pioneer Academy",
            "address": "Santhapuri Nagar, Komarapalayam",
            "rating": "4.9",
            "details": "Typing and more.",
            "location": "Komarapalayam"
        }
    ],
    "Computer": [
        {
            "name": "CSC Computer Education",
            "address": "Vasavi Complex, Komarapalayam",
            "rating": "4.8",
            "details": "Basics, MS Office, internet.",
            "location": "Komarapalayam"
        },
        {
            "name": "IFC Infotech",
            "address": "Salem Main Road, Komarapalayam",
            "rating": "5.0",
            "details": "Hardware & software training.",
            "location": "Komarapalayam"
        },
        {
            "name": "Pioneer Academy",
            "address": "Santhapuri Nagar, Komarapalayam",
            "rating": "4.9",
            "details": "Computer and more.",
            "location": "Komarapalayam"
        }
    ],
    "Tailoring": [
        {
            "name": "Anubi Designing Institute",
            "address": "East Colony, Komarapalayam",
            "rating": "5.0",
            "details": "Tailoring and fashion.",
            "location": "Komarapalayam"
        },
        {
            "name": "Aparnaa Costume Designer",
            "address": "Nasiyanur Rd, Erode",
            "rating": "4.9",
            "details": "Highly rated tailoring institute.",
            "location": "Erode"
        },
        {
            "name": "Apurvaa Tailoring Institute",
            "address": "Brough Rd, Erode",
            "rating": "5.0",
            "details": "Tailoring & Beautician training.",
            "location": "Erode"
        },
        {
            "name": "Janani Designers",
            "address": "Komarapalayam",
            "rating": "4.8",
            "details": "Fashion & stitching.",
            "location": "Komarapalayam"
        },
        {
            "name": "BE Relax Tailoring",
            "address": "Bhavani, Tamil Nadu",
            "rating": "4.5",
            "details": "Tailoring center.",
            "location": "Bhavani"
        },
        {
            "name": "Agni Poo Institute",
            "address": "Opp. PGR Hospital, Bhavani",
            "rating": "5.0",
            "details": "Designer and tailoring.",
            "location": "Bhavani"
        },
        {
            "name": "Aarah Aari Institute",
            "address": "KK Nagar, Bhavani",
            "rating": "5.0",
            "details": "Tailoring and embroidery.",
            "location": "Bhavani"
        }
    ],
    "Dance": [
        {
            "name": "Senz X Dance Class",
            "address": "Apex Colony, Komarapalayam",
            "rating": "4.8",
            "details": "Dance classes.",
            "location": "Komarapalayam"
        },
        {
            "name": "Maaran Dance Studio",
            "address": "Salem Main Road, Komarapalayam",
            "rating": "5.0",
            "details": "Dance studio.",
            "location": "Komarapalayam"
        },
        {
            "name": "Dance Dreamers",
            "address": "Near Saravana Theatre, Komarapalayam",
            "rating": "5.0",
            "details": "Dance training.",
            "location": "Komarapalayam"
        }
    ]
}

# Show results
if selected_category:
    st.subheader(f"📂 {selected_category} - {selected_location}")
    results = [
        center for center in learning_centers[selected_category]
        if center["location"] == selected_location
    ]
    if results:
        for center in results:
            st.markdown(f"🏫 **{center['name']}**")
            st.markdown(f"📍 Address: {center['address']}")
            st.markdown(f"⭐ Rating: {center['rating']}")
            st.markdown(f"📝 {center['details']}")
            st.markdown("---")
    else:
        st.info("No centers found for this category and location.")





