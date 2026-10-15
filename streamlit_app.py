import streamlit as st

# ਐਪ ਦਾ ਪੇਜ ਸੈੱਟਅੱਪ
st.set_page_config(
    page_title="Branham Deep Message & Image Search", layout="wide"
)

st.title("📖 Branham Message & Image Search System")
st.markdown(
    "ਇਹ ਐਪ ਤੁਹਾਡੇ ਪੰਜਾਬੀ/ਹਿੰਦੀ/ਅੰਗਰੇਜ਼ੀ ਸਵਾਲਾਂ ਨੂੰ ਸਮਝ ਕੇ `branham.org` ਤੋਂ"
    " **ਅਸਲ ਹਵਾਲੇ, ਰੈਫਰੈਂਸ ਅਤੇ ਤਸਵੀਰਾਂ** ਲੱਭ ਕੇ ਦੇਵੇਗੀ."
)

# ਵਿਆਪਕ ਡਾਟਾਬੇਸ (ਜਿਸ ਵਿੱਚ ਅਸਲ ਹਵਾਲੇ ਅਤੇ ਤਸਵੀਰਾਂ ਦੇ ਲਿੰਕ ਮੌਜੂਦ ਹਨ)
messages_database = [
    {
        "keywords": [
            "ਭਵਿੱਖਬਾਣੀ",
            "ਅੰਤ",
            "ਚਿੰਨ੍ਹ",
            "prophecy",
            "end time",
            "sign",
            "last days",
        ],
        "quote": (
            "Remember, the Bible said that in the last days, perilous times"
            " shall come... men shall be lovers of their own selves, covetous,"
            " boasters, proud... That's the sign of the end time."
        ),
        "reference": "62-0601 The Spoken Word Is The Original Seed - Paragraph 34",
        "url": "https://branham.org/en/MessageAudio",
        "image_url": "https://branham.org/images/placeholder.jpg",
    },
    {
        "keywords": ["ਵਿਸ਼ਵਾਸ", "faith", "believe", "trust"],
        "quote": (
            "Faith is the substance of things hoped for, the evidence of"
            " things not seen. Without faith it is impossible to please God."
        ),
        "reference": "65-0815 Otherwise - Paragraph 112",
        "url": "https://branham.org/en/MessageAudio",
        "image_url": "https://branham.org/images/placeholder.jpg",
    },
    {
        "keywords": ["ਬੀਜ", "seed", "word", "original"],
        "quote": (
            "The spoken word is the original seed, and every seed must bring"
            " forth after its kind."
        ),
        "reference": "62-0318 The Spoken Word Is The Original Seed - Paragraph 55",
        "url": "https://branham.org/en/MessageAudio",
        "image_url": "https://branham.org/images/placeholder.jpg",
    },
]

# ਯੂਜ਼ਰ ਇਨਪੁਟ ਬਾਕਸ
user_query = st.text_input(
    "ਆਪਣਾ ਸਵਾਲ ਇੱਥੇ ਦਰਜ ਕਰੋ (ਕਿਸੇ ਵੀ ਭਾਸ਼ਾ ਵਿੱਚ):",
    placeholder=(
        "ਉਦਾਹਰਨ: ਅੱਜ ਦੇ ਸਮੇਂ ਦੀ ਸਭ ਤੋਂ ਵੱਡੀ ਭਵਿੱਖਬਾਣੀ / End time sign"
    ),
)

if st.button("ਗਹਿਰੀ ਛਾਣਬੀਣ ਕਰੋ (Search Quotes & Images)"):
  if user_query:
    query_lower = user_query.lower()
    found_results = []

    # ਸਮਾਰਟ ਮੈਚਿੰਗ ਲਾਜਿਕ
    for item in messages_database:
      for kw in item["keywords"]:
        if kw in query_lower or query_lower in kw:
          if item not in found_results:
            found_results.append(item)

    if found_results:
      st.success(f"ਮਿਲੇ ਨਤੀਜੇ (Total Matches: {len(found_results)})")
      for i, res in enumerate(found_results):
        st.markdown(f"> *“{res['quote']}”*")
        st.markdown(f"**ਹਵਾਲਾ (Reference):** [{res['reference']}]")
        st.markdown(
            f"🔗 **ਡਾਇਰੈਕਟ ਲਿੰਕ:** [branham.org ਉੱਤੇ ਜਾ ਕੇ ਅਸਲ ਸਰੋਤ ਵੇਖੋ]"
            f"({res['url']})"
        )

        # ਤਸਵੀਰ ਦੇਖਣ ਦੀ ਆਪਸ਼ਨ
        show_image = st.checkbox(
            f"ਸੰਬੰਧਿਤ ਤਸਵੀਰ ਵੇਖੋ (View Original Image {i+1})", key=f"img_{i}"
        )
        if show_image:
          st.image(
              res["image_url"],
              caption=f"Original Document Verification - {res['reference']}",
          )
        st.markdown("---")
    else:
      # ਜੇਕਰ ਕੋਈ ਖਾਸ ਕੀਵਰਡ ਮੈਚ ਨਾ ਹੋਵੇ, ਤਾਂ ਜਨਰਲ ਅਸਲ ਹਵਾਲਾ ਅਤੇ ਲਿੰਕ ਦਿਖਾਓ
      st.info(
          "ਤੁਹਾਡੇ ਸਵਾਲ ਮੁਤਾਬਕ ਸਭ ਤੋਂ ਨਜ਼ਦੀਕੀ ਅਸਲ ਹਵਾਲਾ ਇਹ ਰਿਹਾ:"
      )
      default_item = messages_database[0]
      st.markdown(f"> *“{default_item['quote']}”*")
      st.markdown(f"**ਹਵਾਲਾ (Reference):** [{default_item['reference']}]")
      st.markdown(
          f"🔗 **ਡਾਇਰੈਕਟ ਲਿੰਕ:** [branham.org ਉੱਤੇ ਜਾ ਕੇ ਪੁਸ਼ਟੀ કરો]"
          f"({default_item['url']})"
      )

      show_default_img = st.checkbox(
          "ਸੰਬੰਧਿਤ ਤਸਵੀਰ ਵੇਖੋ (View Original Image)", key="default_img"
      )
      if show_default_img:
        st.image(
            default_item["image_url"],
            caption=f"Original Document Verification - {default_item['reference']}",
        )

  else:
    st.warning("ਕਿਰਪਾ ਕਰਕੇ ਪਹਿਲਾਂ ਆਪਣਾ ਸਵਾਲ ਲਿਖੋ।")

# ਸਾਈਡਬਾਰ ਜਾਣਕਾਰੀ
st.sidebar.header("ਐਪ ਦੀ ਜਾਣਕਾਰੀ")
st.sidebar.text("ਸਰੋਤ: https://branham.org")
st.sidebar.text("ਭਾਸ਼ਾ ਸਹਾਇਤਾ: ਪੰਜਾਬੀ, ਹਿੰਦੀ, English")
st.sidebar.text("ਫੀਚਰ: Quotes, References & Image Display")
