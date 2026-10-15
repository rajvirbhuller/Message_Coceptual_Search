import streamlit as st

# ਐਪ ਦਾ ਪੇਜ ਸੈੱਟਅੱਪ
st.set_page_config(
    page_title="Message Audio & Image Search App", layout="wide"
)

st.title("📖 Message Audio & Image Search System")
st.markdown(
    "ਇਹ ਐਪ 1250+ ਫ਼ਾਈਲਾਂ ਅਤੇ ਤਸਵੀਰਾਂ ਵਿੱਚੋਂ ਤੁਹਾਡੇ ਸਵਾਲ ਮੁਤਾਬਕ **ਅਸਲ ਹਵਾਲੇ"
    " (Original Quotes)** ਲੱਭ ਕੇ ਦੇਵੇਗੀ।"
)

# ਯੂਜ਼ਰ ਇਨਪੁਟ ਬਾਕਸ (ਕਿਸੇ ਵੀ ਭਾਸ਼ਾ ਵਿੱਚ - ਪੰਜਾਬੀ, ਹਿੰਦੀ, ਅੰਗਰੇਜ਼ੀ)
user_query = st.text_input(
    "ਆਪਣਾ ਸਵਾਲ ਇੱਥੇ ਦਰਜ ਕਰੋ:",
    placeholder="ਉਦਾਹਰਨ: Faith, ਵਿਸ਼ਵਾਸ, या विश्वास",
)

if st.button("ਖੋਜ ਕਰੋ (Search)"):
  if user_query:
    st.info(
        f"ਤੁਹਾਡੇ ਸਵਾਲ '{user_query}' ਲਈ ਡਾਟਾਬੇਸ ਵਿੱਚ ਛਾਣਬੀਣ ਕੀਤੀ ਜਾ ਰਹੀ ਹੈ..."
    )

    # ਸਰਚ ਰਿਜ਼ਲਟ
    st.success("ਸਹੀ ਹਵਾਲਾ ਮਿਲਿਆ:")

    # ਅਸਲ ਸ਼ਬਦ (Original Words)
    st.markdown(
        "> *“Original quote text from the message files matching your query..."
        "”*"
    )

    # ਸਪਸ਼ਟ ਰੈਫਰੈਂਸ
    st.markdown(
        "**ਹਵਾਲਾ (Reference):** [Message File Name / Audio Title - Paragraph"
        " Ref]"
    )

    # ਜੇਕਰ ਜਵਾਬ ਨਾਲ ਕੋਈ ਤਸਵੀਰ ਜੁੜੀ ਹੋਵੇ ਤਾਂ ਉਸਨੂੰ ਵੇਖਣ ਦਾ ਵਿਕਲਪ
    show_image = st.checkbox("ਸੰਬੰਧਿਤ ਤਸਵੀਰ ਵੇਖੋ (View Original Image)")
    if show_image:
      st.image(
          "https://branham.org/images/placeholder.jpg",
          caption="Original Document/Image Reference Verification",
      )
  else:
    st.warning("ਕਿਰਪਾ ਕਰਕੇ ਪਹਿਲਾਂ ਆਪਣਾ ਸਵਾਲ ਲਿਖੋ।")

# ਸਾਈਡਬਾਰ ਜਾਣਕਾਰੀ
st.sidebar.header("ਐਪ ਦੀ ਜਾਣਕਾਰੀ")
st.sidebar.text("ਕੁੱਲ ਫਾਈਲਾਂ: 1250+")
st.sidebar.text("ਭਾਸ਼ਾ ਸਹਾਇਤਾ: ਪੰਜਾਬੀ, ਹਿੰਦੀ, English")
st.sidebar.text("ਵਿਸ਼ੇਸ਼ਤਾ: Original Quotes & Image Verification")
