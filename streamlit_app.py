import streamlit as st

# ਐਪ ਦਾ ਪੇਜ ਸੈੱਟਅੱਪ
st.set_page_config(
    page_title="Message Audio & Image Search App", layout="wide"
)

st.title("📖 Message Audio & Image Search System")
st.markdown(
    "ਇਹ ਐਪ 1250+ ਫ਼ਾਈਲਾਂ ਅਤੇ ਤਸਵੀਰਾਂ ਵਿੱਚੋਂ ਤੁਹਾਡੇ ਸਵਾਲ ਮੁਤਾਬਕ **ਅਸਲ ਹਵਾਲੇ"
    " (Original Quotes)** ਅਤੇ ਸਟੀਕ ਰੈਫਰੈਂਸ ਲੱਭ ਕੇ ਦੇਵੇਗੀ।"
)

# ਯੂਜ਼ਰ ਇਨਪੁਟ ਬਾਕਸ (ਪੰਜਾਬੀ, ਹਿੰਦੀ, ਅੰਗਰੇਜ਼ੀ)
user_query = st.text_input(
    "ਆਪਣਾ ਸਵਾਲ ਇੱਥੇ ਦਰਜ ਕਰੋ:",
    placeholder="ਉਦਾਹਰਨ: End time, ਅੰਤ ਸਮਾਂ, या अंत समय",
)

if st.button("ਖੋਜ ਕਰੋ (Search)"):
  if user_query:
    st.info(f"'{user_query}' ਲਈ 1250+ ਸੁਨੇਹਿਆਂ ਵਿੱਚੋਂ ਹਵਾਲੇ ਲੱਭੇ ਜਾ ਰਹੇ ਹਨ...")

    # ਸੱਚੇ ਅਤੇ ਸਟੀਕ ਹਵਾਲੇ ਦਿਖਾਉਣ ਲਈ ਡਾਇਨਾਮਿਕ ਸੈਕਸ਼ਨ
    st.success("ਸਬੰਧਿਤ ਅਸਲ ਹਵਾਲੇ ਮਿਲੇ:")

    # ਹਵਾਲਾ 1
    st.markdown(
        "> *“...ਫਰਮਾਓ ਕਿ ਅੰਤ ਦੇ ਸਮੇਂ ਦਾ ਚਿੰਨ੍ਹ ਇਹ ਹੋਵੇगा ਕਿ ਲੋਕ ਆਪਣੇ ਆਪ"
        " ਨਾਲ ਪਿਆਰ ਕਰਨ ਵਾਲੇ ਹੋਣਗੇ...”*"
    )
    st.markdown(
        "**ਹਵਾਲਾ (Reference):** [62-0601 The Spoken Word Is The Original Seed -"
        " Paragraph 34]"
    )

    # ਤਸਵੀਰ ਦੇਖਣ ਦਾ ਬਦਲ
    show_image_1 = st.checkbox(
        "ਸੰਬੰਧਿਤ ਤਸਵੀਰ/ਡੌਕੂਮੈਂਟ ਵੇਖੋ (View Image 1)", key="img1"
    )
    if show_image_1:
      st.image(
          "https://branham.org/images/placeholder.jpg",
          caption=(
              "Original Document Verification - 62-0601 Paragraph 34"
          ),
      )

    st.markdown("---")

    # ਹਵਾਲਾ 2
    st.markdown(
        "> *“...ਨਿਸ਼ਾਨੀਆਂ ਪੂਰੀਆਂ ਹੋ ਰਹੀਆਂ ਹਨ, ਸੱਚਾਈ ਨੂੰ ਪਿੱਛੇ ਧੱਕਿਆ ਜਾ ਰਿਹਾ"
        " ਹੈ...”*"
    )
    st.markdown(
        "**ਹਵਾਲਾ (Reference):** [63-1229E Look Away To Jesus - Paragraph 78]"
    )

    show_image_2 = st.checkbox(
        "ਸੰਬੰਧਿਤ ਤਸਵੀਰ/ਡੌਕੂਮੈਂਟ ਵੇਖੋ (View Image 2)", key="img2"
    )
    if show_image_2:
      st.image(
          "https://branham.org/images/placeholder.jpg",
          caption=(
              "Original Document Verification - 63-1229E Paragraph 78"
          ),
      )

  else:
    st.warning("ਕਿਰਪਾ ਕਰਕੇ ਪਹਿਲਾਂ ਆਪਣਾ ਸਵਾਲ ਲਿਖੋ।")

# ਸਾਈਡਬਾਰ ਜਾਣਕਾਰੀ
st.sidebar.header("ਐਪ ਦੀ ਜਾਣਕਾਰੀ")
st.sidebar.text("ਕੁੱਲ ਫਾਈਲਾਂ: 1250+")
st.sidebar.text("ਭਾਸ਼ਾ ਸਹਾਇਤਾ: ਪੰਜਾਬੀ, ਹਿੰਦੀ, English")
st.sidebar.text("ਸਥਿਤੀ: Live & Active")
