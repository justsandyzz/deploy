import streamlit as st

# Title and Description
st.set_page_config(page_title="Badminton Injury & Skill Enhancer", layout="wide")
st.title("🏸 Smart Injury Prediction & Skill Enhancement System")
st.markdown("Built for badminton players to stay injury-free and level up their game!")

# Sidebar Navigation
st.sidebar.title("Navigation")
option = st.sidebar.radio("Go to:", [
    "🏠 Home", 
    "📊 Injury Prediction", 
    "💪 Skill Enhancer", 
    "📷 Posture Correction", 
    "ℹ️ About"
])

# Home
if option == "🏠 Home":
    st.header("Welcome 👋")
    st.image("https://upload.wikimedia.org/wikipedia/commons/5/56/Badminton_racket_and_shuttlecock.jpg", use_column_width=True)
    st.markdown("""
    ### This system helps players:
    - 🧠 Predict injury risk
    - 💪 Improve playing techniques
    - 🎯 Get posture correction using video/image
    """)
    st.success("Start by choosing an option from the left sidebar.")

# Injury Prediction
elif option == "📊 Injury Prediction":
    st.header("📊 Injury Risk Assessment")

    st.subheader("Enter Player Details:")
    age = st.slider("Player Age", 10, 40, 18)
    training_hours = st.slider("Training hours/week", 0, 30, 10)
    previous_injuries = st.selectbox("Any previous injuries?", ["None", "Minor", "Major"])
    intensity = st.radio("Training Intensity", ["Low", "Medium", "High"])

    if st.button("Predict Injury Risk"):
        # Placeholder logic – replace with ML model
        st.info("Prediction running... (ML model integration pending)")

        # Dummy result
        st.success("Predicted Injury Risk: 45%")
        st.caption("⚠️ This is a sample result. Actual ML model will provide real predictions.")

# Skill Enhancer
elif option == "💪 Skill Enhancer":
    st.header("💪 Skill Enhancement Suggestions")

    play_style = st.selectbox("Select your play style", ["Attacker", "Defender", "All-rounder"])
    st.write("Here are some training recommendations:")

    if play_style == "Attacker":
        st.markdown("""
        - 🏋️ Smash power drills  
        - 🏃‍♂️ Fast footwork training  
        - 🧠 Reaction time exercises
        """)
    elif play_style == "Defender":
        st.markdown("""
        - 🧱 Defense wall drills  
        - 🕸 Net block precision  
        - 💨 Lateral movement work
        """)
    else:
        st.markdown("""
        - ⚖️ Balance & control sessions  
        - 🧘 Flexibility and core stability  
        - 🔁 Endurance training
        """)

# Posture Correction
elif option == "📷 Posture Correction":
    st.header("📷 Posture Feedback Module")
    st.write("Upload a video or image for posture analysis:")

    file = st.file_uploader("Upload Image or Video", type=["jpg", "png", "mp4", "avi"])

    if file is not None:
        file_type = file.type

        if file_type.startswith("image"):
            st.image(file, caption="Uploaded Image", use_column_width=True)
            st.info("Analyzing posture... (DL model integration pending)")
            st.success("Feedback: Raise your racket higher on serve to reduce shoulder stress.")
        elif file_type.startswith("video"):
            st.video(file)
            st.info("Analyzing motion and posture... (DL model integration pending)")
            st.success("Feedback: Improve ankle posture during lunges to avoid sprains.")
        else:
            st.error("Unsupported file format.")

# About
elif option == "ℹ️ About":
    st.header("📌 About This Project")
    st.markdown("""
    This project aims to:
    - Prevent injuries in badminton through AI
    - Offer personalized training recommendations
    - Analyze gameplay videos or images for posture correction  
    Built using **Streamlit**, **Python**, and will include **ML/DL integration**.
    """)

    st.markdown("Created by: Santhosh P and Sibi R")

