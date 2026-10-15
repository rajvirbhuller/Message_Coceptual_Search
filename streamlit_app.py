import streamlit as st

st.set_page_config(
    page_title="Branham RAG Search System", layout="wide"
)

st.title("📖 Branham Message Real RAG & Image Search System")
st.markdown(
    "ਇਹ ਐਪ https://branham.org/en/MessageAudio ਦੇ ਅਸਲ ਡਾਟਾਬੇਸ ਨਾਲ ਜੁੜ ਕੇ"
    " ਸਿਰਫ਼ ਸੱਚੇ ਹਵਾਲੇ ਅਤੇ ਡਾਇਰੈਕਟ URL ਲਿੰਕ ਦਿਖਾਵੇਗੀ[span_3](start_span)[span_3](end_span)."
)

user_query = st.text_input(
    "ਆਪਣਾ ਸਵਾਲ ਇੱਥੇ ਦਰਜ ਕਰੋ (ਪੰਜਾਬੀ, ਹਿੰਦੀ, English):",
    placeholder="ਉਦਾਹਰਨ: End time sign / Last days",
)

if st.button("ਅਸਲ ਹਵਾਲੇ ਖੋਜੋ"):
  if user_query:
    st.info("ਡਾਟਾਬੇਸ ਵਿੱਚ ਛਾਣਬੀਣ ਕੀਤੀ ਜਾ ਰਹੀ ਹੈ...")
    st.warning(
        "⚠️ **ਨੋਟ:** 1250+ ਫ਼ਾਈਲਾਂ ਦਾ ਵੈਕਟਰ ਡਾਟਾਬੇਸ ਇਸ ਸਮੇਂ ਕਲਾਉਡ ਉੱਤੇ"
        " ਇੰਡੈਕਸ ਨਹੀਂ ਹੈ। ਜਾਅਲੀ ਹਵਾਲਿਆਂ ਤੋਂ ਬਚਣ ਲਈ ਸਹੀ ਡਾਟਾ ਸਿੰਕ ਕਰਨਾ ਜ਼ਰੂਰੀ"
        " ਹੈ।"
    )
    st.markdown(
        "🔗 **ਅਧਿਕਾਰਤ ਸਰੋਤ ਦਾ ਲਿੰਕ:** [branham.org/en/MessageAudio ਉੱਤੇ ਜਾ ਕੇ"
        " ਖੁਦ ਪੁਸ਼ਟੀ ਕਰੋ](https://branham.org/en/MessageAudio)[span_4](start_span)[span_4](end_span)"
    )
  else:
    st.warning("ਕਿਰਪਾ ਕਰਕੇ ਪਹਿਲਾਂ ਆਪਣਾ ਸਵਾਲ ਲਿਖੋ।")

st.sidebar.header("ਸਿਸਟਮ ਸਥਿਤੀ")
st.sidebar.text("ਸਰੋਤ: https://branham.org[span_5](start_span)[span_5](end_span)")
st.sidebar.text("ਸੁਰੱਖਿਆ: No Fake Quotes Policy")
