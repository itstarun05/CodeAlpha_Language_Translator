import streamlit as st
from deep_translator import GoogleTranslator

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍",
    layout="centered"
)

# ----------------------------
# Custom CSS
# ----------------------------
st.markdown("""
<style>
.main {
    padding-top: 20px;
}
h1 {
    text-align:center;
    color:#4CAF50;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# Title
# ----------------------------
st.title("🌍 AI Language Translator")
st.write("Translate text into multiple languages instantly using Google Translator.")

# ----------------------------
# Languages
# ----------------------------
languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Italian": "it",
    "Japanese": "ja",
    "Chinese": "zh-CN",
    "Russian": "ru",
    "Arabic": "ar",
    "Korean": "ko",
    "Punjabi": "pa",
    "Urdu": "ur",
    "Tamil": "ta",
    "Telugu": "te",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Bengali": "bn"
}

# ----------------------------
# Dropdowns
# ----------------------------
source = st.selectbox(
    "🌐 Source Language",
    list(languages.keys()),
    index=0
)

target = st.selectbox(
    "🎯 Target Language",
    list(languages.keys()),
    index=1
)

# ----------------------------
# Text Input
# ----------------------------
text = st.text_area(
    "✍ Enter Text",
    height=180,
    placeholder="Type your text here..."
)

# ----------------------------
# Translate
# ----------------------------
if st.button("🚀 Translate", use_container_width=True):

    if text.strip() == "":
        st.warning("⚠ Please enter some text.")

    elif source == target:
        st.info("Source and Target languages are the same.")

    else:

        try:

            translated = GoogleTranslator(
                source=languages[source],
                target=languages[target]
            ).translate(text)

            st.success("✅ Translation Successful")

            st.text_area(
                label="📄 Translated Text",
                value=translated,
                height=180
            )

        except Exception as e:

            st.error(f"❌ Error : {e}")

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.caption("Developed by Tarun | CodeAlpha AI Internship")