import streamlit as st
import joblib

# Load trained model
model = joblib.load("spam_model.pkl")

st.set_page_config(
    page_title="AI Spam Detector",
    page_icon="🛡️"
)

st.title("🛡️ AI-Based Spam Detection System")
st.write("Enter a message below to check whether it is Spam or Ham.")

message = st.text_area("Enter your message:")

if st.button("Check Message"):
    if message.strip() == "":
        st.warning("Please enter a message.")
    else:
        prediction = model.predict([message])[0]

        if prediction == "spam":
            st.error("🚨 SPAM MESSAGE")
        else:
            st.success("✅ HAM — LEGITIMATE MESSAGE")