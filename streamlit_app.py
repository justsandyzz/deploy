import streamlit as st

# Page settings
st.set_page_config(page_title="Smart Injury & Skill Enhancement System", layout="wide")
st.title("🏅 Smart Injury Prediction & Skill Enhancement System")
st.markdown("Built to help athletes of all sports stay injury-free and improve their performance.")

# Sidebar navigation
st.sidebar.title("Navigation")
option = st.sidebar.radio("Go to:", [
    "🏠 Home", 
    "📊 Injury Prediction", 
    "💪 Skill Enhancer", 
    "📷 Posture Correction", 
    "ℹ️ About"
])

# Home Section
if option == "🏠 Home":
    st.header("Welcome 👋")

    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/e/e7/Sports_collage.jpg", 
        caption="Train Smart. Stay Strong.", 
        use_container_width=True
    )

    st.markdown("""
    ### This system helps athletes:
    - 🧠 Predict injury risk  
    - 💪 Improve sport-specific techniques  
    - 🎯 Get posture correction using video/image analysis
    """)

    st.success("Start by choosing an option from the left sidebar.")

# Injury Prediction Section
elif option == "📊 Injury Prediction":
    st.header("📊 Injury Risk Assessment")

    st.subheader("Enter Athlete Details:")
    age = st.slider("Athlete Age", 10, 60, 25)
    training_hours = st.slider("Training hours/week", 0, 40, 10)
    previous_injuries = st.selectbox("Any previous injuries?", ["None", "Minor", "Major"])
    intensity = st.radio("Training Intensity", ["Low", "Medium", "High"])

    if st.button("Predict Injury Risk"):
        # Placeholder logic – replace with your ML model later
        st.info("Running prediction model...")

        # Dummy result
        st.success("Predicted Injury Risk: 42%")
        st.caption("⚠️ This is a sample result. Actual ML model will give personalized prediction.")

# Skill Enhancer Section
elif option == "💪 Skill Enhancer":
    st.header("💪 Skill Enhancement Suggestions")

    play_style = st.selectbox("Select your play/training style", [
        "Strength-focused", "Agility-focused", "Endurance-focused", "All-rounder"
    ])
    st.write("Based on your selection, here are general suggestions:")

    if play_style == "Strength-focused":
        st.markdown("""
        - 🏋️ Resistance training  
        - 🧱 Power drills  
        - 🧘‍♂️ Muscle recovery sessions
        """)
    elif play_style == "Agility-focused":
        st.markdown("""
        - 🔄 Ladder drills  
        - 🤸 Core coordination  
        - 🧠 Reflex and reaction training
        """)
    elif play_style == "Endurance-focused":
        st.markdown("""
        - 🏃 Interval runs  
        - 🌀 Cardiovascular circuits  
        - ⏱ Long-duration stamina building
        """)
    else:
        st.markdown("""
        - ⚖️ Balance and stability  
        - 🔁 Hybrid workout circuits  
        - 🧘‍♂️ Flexibility and core conditioning
        """)

# Posture Correction Section
elif option == "📷 Posture Correction":
    st.header("📷 Posture Feedback Module")
    st.write("Upload a video or image of the athlete to analyze posture and prevent injuries.")

    file = st.file_uploader("Upload an image or video", type=["jpg", "png", "mp4", "avi"])

    if file is not None:
        file_type = file.type

        if file_type.startswith("image"):
            st.image(file, caption="Uploaded Image", use_container_width=True)
            st.info("Analyzing posture... (DL model integration pending)")
            st.success("Feedback: Adjust shoulder alignment during movement to avoid overuse injury.")
        elif file_type.startswith("video"):
            st.video(file)
            st.info("Analyzing motion and posture... (DL model integration pending)")
            st.success("Feedback: Consider lighter landings to protect knees and ankles.")
        else:
            st.error("Unsupported file format.")

# About Section
elif option == "ℹ️ About":
    st.header("📌 About This Project")
    st.markdown("""
    This project supports athletes across all sports by using AI to:
    - 🧠 Predict injury likelihood  
    - 🛠 Recommend skill improvements  
    - 📷 Analyze posture and technique from visual input  
      
    Built with **Python**, **Streamlit**, and will soon integrate **ML/DL models**.
    """)

    st.markdown("Created by: `Your Name`")
