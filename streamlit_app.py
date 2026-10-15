import os
import streamlit as st

# ਐਪ ਦਾ ਪੇਜ ਸੈੱਟਅੱਪ
st.set_page_config(
    page_title="Branham RAG Search System", layout="wide"
)

st.title("📖 Branham Message Real RAG & Image Search System")
st.markdown(
    "ਇਹ ਐਪ `https://branham.org/en/MessageAudio` ਦੇ ਅਸਲ ਡਾਟਾਬੇਸ ਨਾਲ ਜੁੜ ਕੇ"
    " ਸਿਰਫ਼ ਸੱਚੇ ਹਵਾਲੇ ਅਤੇ ਡਾਇਰੈਕਟ URL [Uniform Resource Locator] ਲਿੰਕ ਦਿਖਾਵੇਗੀ।"
    [span_2](start_span)"[span_2](end_span)"
)

# ਯੂਜ਼ਰ ਇਨਪੁਟ ਬਾਕਸ
user_query = st.text_input(
    "ਆਪਣਾ ਸਵਾਲ ਇੱਥੇ ਦਰਜ ਕਰੋ (ਪੰਜਾਬੀ, ਹਿੰਦੀ, English):",
    placeholder=(
        "ਉਦਾਹਰਨ: ਅੰਤ ਦੇ ਸਮੇਂ ਦਾ ਚਿੰਨ੍ਹ / End time sign / Last days"
    ),
)

if st.button("ਅਸਲ ਹਵਾਲੇ ਖੋਜੋ (Search RAG Database)"):
  if user_query:
    st.info(
        f"'{user_query}' ਲਈ branham.org ਦੇ ਅਸਲ ਰਿਕਾਰਡਾਂ ਵਿੱਚੋਂ ਛਾਣਬੀਣ ਕੀਤੀ ਜਾ"
        " ਰਹੀ ਹੈ..."
    )

    # ਸਿਸਟਮ ਸਟੇਟਸ (ਜਦੋਂ ਤੱਕ ਡਾਟਾਬੇਸ ਲੋਡ ਨਹੀਂ ਹੁੰਦਾ)
    st.warning(
        "⚠️ **ਨੋਟ:** ਅਜੇ 1250+ ਫ਼ਾਈਲਾਂ ਦਾ ਲੋਕਲ ਵੈਕਟਰ ਡਾਟਾਬੇਸ (Vector Database)"
        " ਇਸ ਕਲਾਉਡ ਸਰਵਰ ਉੱਤੇ ਇੰਡੈਕਸ ਨਹੀਂ ਹੋਇਆ। ਇਸ ਲਈ ਸਿਸਟਮ ਜਾਅਲੀ ਹਵਾਲੇ"
        " ਦਿਖਾਉਣ ਦੀ ਬਜਾਏ ਤੁਹਾਨੂੰ ਸਹੀ ਸਟੇਟਸ ਦੱਸ ਰਿਹਾ ਹੈ।"
    )

    st.markdown(
        "ਜਦੋਂ ਅਸੀਂ ਇਸ ਵਿੱਚ ਪੂਰਾ ਸਕ੍ਰਿਪਪਿੰਗ ਅਤੇ ਇੰਡੈਕਸਿੰਗ ਕੋਡ (PDF/Text Parser)"
        " ਜੋੜ ਦੇਵਾਂਗੇ, ਤਾਂ ਇਹ ਬਿਲਕੁਲ ਸਹੀ ਲਾਈਨਾਂ ਅਤੇ **branham.org** ਦੇ"
        " ਅਸਲ ਲਿੰਕ ਲੱਭ ਕੇ ਦੇਵੇਗਾ[span_3](start_span)[span_3](end_span)."
    )

    # ਸਹੀ ਸਰੋਤ ਦਾ ਨਮੂਨਾ ਲਿੰਕ
    st.markdown(
        "🔗 **ਅਧਿਕਾਰਤ ਸਰੋਤ ਦਾ ਲਿੰਕ:** [branham.org/en/MessageAudio ਉੱਤੇ ਜਾ ਕੇ"
        " ਖੁਦ ਪੁਸ਼ਟੀ ਕਰੋ](https://branham.org/en/MessageAudio)[span_4](start_span)[span_4](end_span)"
    )

  else:
    st.warning("ਕਿਰਪਾ ਕਰਕੇ ਪਹਿਲਾਂ ਆਪਣਾ ਸਵਾਲ ਲਿਖੋ।")

# ਸਾਈਡਬਾਰ ਜਾਣਕਾਰੀ
st.sidebar.header("ਸਿਸਟਮ ਸਥਿਤੀ (System Status)")
st.sidebar.text("ਡਾਟਾਬੇਸ: RAG Pipeline Pending")
st.sidebar.text("ਸਰੋਤ: https://branham.org[span_5](start_span)[span_5](end_span)")
st.sidebar.text("ਸੁਰੱਖਿਆ: No Fake Quotes Policy Active")
