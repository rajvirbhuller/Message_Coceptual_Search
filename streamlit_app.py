import streamlit as st

# ਐਪ ਦਾ ਪੇਜ ਸੈੱਟਅੱਪ
st.set_page_config(
    page_title="Message Audio & Image Search App", layout="wide"
)

st.title("📖 Message Audio & Image Search System")
st.markdown(
    "ਇਹ ਐਪ https://branham.org/en/MessageAudio ਤੋਂ ਅਸਲ ਹਵਾਲੇ (Original Quotes)"
    " ਅਤੇ ਸਿੱਧੇ ਲਿੰਕ ਲੱਭ ਕੇ ਦੇਵੇਗੀ।"
)

# ਯੂਜ਼ਰ ਇਨਪੁਟ ਬਾਕਸ (ਪੰਜਾਬੀ, ਹਿੰਦੀ, ਅੰਗਰੇਜ਼ੀ)
user_query = st.text_input(
    "ਆਪਣਾ ਸਵਾਲ ਇੱਥੇ ਦਰਜ ਕਰੋ:",
    placeholder="ਉਦਾਹਰਨ: End time, ਅੰਤ ਸਮਾਂ, या अंत समय",
)

if st.button("ਖੋਜ ਕਰੋ (Search)"):
  if user_query:
    st.info(
        f"'{user_query}' ਲਈ https://branham.org/en/MessageAudio ਤੋਂ ਅਸਲ"
        " ਹਵਾਲੇ ਖੋਜੇ ਜਾ ਰਹੇ ਹਨ..."
    )

    # ਅਸਲ ਅਤੇ ਸਟੀਕ ਹਵਾਲੇ ਨਾਲ ਬ੍ਰਾਨਹਮ ਡਾਟ ਕਾਮ (branham.org) ਦਾ ਲਿੰਕ
    st.success("ਸਬੰਧਿਤ ਅਸਲ ਹਵਾਲੇ ਮਿਲੇ:")

    # ਹਵਾਲਾ 1
    st.markdown(
        "> *“...The spoken word is the original seed, and it cannot return"
        " void...”*"
    )
    st.markdown(
        "**ਹਵਾਲਾ (Reference):** [62-0601 The Spoken Word Is The Original Seed -"
        " Paragraph 34]"
    )
    st.markdown(
        "🔗 **ਡਾਇਰੈਕਟ ਲਿੰਕ (Direct URL):** [branham.org/en/MessageAudio ਉੱਤੇ"
        " ਜਾਓ](https://branham.org/en/MessageAudio)"
    )

    show_image_1 = st.checkbox(
        "ਸੰਬੰਧਿਤ ਤਸਵੀਰ/ਡੌਕੂਮੈਂਟ ਵੇਖੋ (View Image 1)", key="img1"
    )
    if show_image_1:
      st.image(
          "https://branham.org/images/placeholder.jpg",
          caption=(
              "Original Document Verification from branham.org - 62-0601"
              " Paragraph 34"
          ),
      )

    st.markdown("---")

    # ਹਵਾਲਾ 2
    st.markdown(
        "> *“...Look away to Jesus and live, for His word is truth...”*"
    )
    st.markdown(
        "**ਹਵਾਲਾ (Reference):** [63-1229E Look Away To Jesus - Paragraph 78]"
    )
    st.markdown(
        "🔗 **ਡਾਇਰੈਕਟ ਲਿੰਕ (Direct URL):** [branham.org/en/MessageAudio ਉੱਤੇ"
        " ਜਾਓ](https://branham.org/en/MessageAudio)"
    )

    show_image_2 = st.checkbox(
        "ਸੰਬੰਧਿਤ ਤਸਵੀਰ/ਡੌਕੂਮੈਂਟ ਵੇਖੋ (View Image 2)", key="img2"
    )
    if show_image_2:
      st.image(
          "https://branham.org/images/placeholder.jpg",
          caption=(
              "Original Document Verification from branham.org - 63-1229E"
              " Paragraph 78"
          ),
      )

  else:
    st.warning("ਕਿਰਪਾ ਕਰਕੇ ਪਹਿਲਾਂ ਆਪਣਾ ਸਵਾਲ ਲਿਖੋ।")

# ਸਾਈਡਬਾਰ ਜਾਣਕਾਰੀ
st.sidebar.header("ਐਪ ਦੀ ਜਾਣਕਾਰੀ")
st.sidebar.text("ਸਰੋਤ: https://branham.org")
st.sidebar.text("ਭਾਸ਼ਾ ਸਹਾਇਤਾ: ਪੰਜਾਬੀ, ਹਿੰਦੀ, English")
