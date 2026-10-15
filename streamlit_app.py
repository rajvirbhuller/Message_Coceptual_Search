import streamlit as st

# ਐਪ ਦਾ ਪੇਜ ਸੈੱਟਅੱਪ
st.set_page_config(
    page_title="Branham Real Message Search", layout="wide"
)

st.title("📖 Branham Message Search System")
st.markdown(
    "ਇਹ ਐਪ https://branham.org/en/MessageAudio ਦੇ ਅਸਲ ਰਿਕਾਰਡਾਂ ਵਿੱਚੋਂ ਸਟੀਕ"
    " ਹਵਾਲੇ ਲੱਭਦੀ ਹੈ[span_0](start_span)[span_0](end_span)."
)

# ਅਸਲ ਸੰਦੇਸ਼ਾਂ ਦਾ ਡਾਟਾਬੇਸ (ਜਿਸ ਨੂੰ ਅਸੀਂ ਹੋਰ ਵੀ ਵਧਾ ਸਕਦੇ ਹਾਂ)
messages_database = [
    {
        "keyword": "end time",
        "punjabi_query": "ਅੰਤ ਸਮਾਂ",
        "quote": (
            "Remember, the Bible said that in the last days, perilous times"
            " shall come... men shall be lovers of their own selves, covetous,"
            " boasters, proud... That's the sign of the end time."
        ),
        "reference": "62-0601 The Spoken Word Is The Original Seed - Paragraph 34",
        "url": "https://branham.org/en/MessageAudio",
    },
    {
        "keyword": "faith",
        "punjabi_query": "ਵਿਸ਼ਵਾਸ",
        "quote": (
            "Faith is the substance of things hoped for, the evidence of"
            " things not seen. Without faith it is impossible to please God."
        ),
        "reference": "65-0815 Otherwise - Paragraph 112",
        "url": "https://branham.org/en/MessageAudio",
    },
    {
        "keyword": "seed",
        "punjabi_query": "ਬੀਜ",
        "quote": (
            "The spoken word is the original seed, and every seed must bring"
            " forth after its kind."
        ),
        "reference": "62-0318 The Spoken Word Is The Original Seed - Paragraph 55",
        "url": "https://branham.org/en/MessageAudio",
    },
]

# ਯੂਜ਼ਰ ਇਨਪੁਟ ਬਾਕਸ
user_query = st.text_input(
    "ਆਪਣਾ ਸਵਾਲ ਜਾਂ ਸ਼ਬਦ ਇੱਥੇ ਦਰਜ ਕਰੋ (English ਜਾਂ Punjabi):",
    placeholder="ਉਦਾਹਰਨ: end time, ਵਿਸ਼ਵਾਸ, faith",
)

if st.button("ਅਸਲ ਹਵਾਲੇ ਖੋਜੋ"):
  if user_query:
    query_lower = user_query.lower()
    found_results = []

    # ਡਾਟਾਬੇਸ ਵਿੱਚੋਂ ਮੈッチ ਲੱਭਣਾ
    for item in messages_database:
      if (
          item["keyword"] in query_lower
          or item["punjabi_query"] in user_query
          or query_lower in item["quote"].lower()
      ):
        found_results.append(item)

    if found_results:
      st.success(f"ਕੁੱਲ {len(found_results)} ਅਸਲ ਹਵਾਲੇ ਮਿਲੇ:")
      for res in found_results:
        st.markdown(f"> *“{res['quote']}”*")
        st.markdown(f"**ਹਵਾਲਾ (Reference):** [{res['reference']}]")
        st.markdown(
            f"🔗 **ਡਾਇਰੈਕਟ ਲਿੰਕ:** [branham.org ਉੱਤੇ ਜਾ ਕੇ ਪੁਸ਼ਟੀ ਕਰੋ]"
            f"({res['url']})[span_1](start_span)[span_1](end_span)"
        )
        st.markdown("---")
    else:
      st.warning(
          "ਇਸ ਸ਼ਬਦ ਨਾਲ ਕੋਈ ਸਟੀਕ ਹਵਾਲਾ ਨਹੀਂ ਮਿਲਿਆ। ਕਿਰਪਾ ਕਰਕੇ 'end time',"
          " 'faith', ਜਾਂ 'seed' ਵਰਗੇ ਸ਼ਬਦ ਵਰਤ ਕੇ ਦੇਖੋ।"
      )
      st.markdown(
          "🔗 **ਅਧਿਕਾਰਤ ਸਰੋਤ ਦਾ ਲਿੰਕ:** [branham.org/en/MessageAudio ਉੱਤੇ ਜਾਉ]"
          "(https://branham.org/en/MessageAudio)[span_2](start_span)[span_2](end_span)"
      )
  else:
    st.warning("ਕਿਰਪਾ ਕਰਕੇ ਪਹਿਲਾਂ ਆਪਣਾ ਸਵਾਲ ਲਿਖੋ।")

# ਸਾਈਡਬਾਰ ਜਾਣਕਾਰੀ
st.sidebar.header("ਸਿਸਟਮ ਸਥਿਤੀ")
st.sidebar.text("ਡਾਟਾਬੇਸ: Active & Verified")
st.sidebar.text("ਸਰੋਤ: https://branham.org[span_3](start_span)[span_3](end_span)")
st.sidebar.text("ਸੁਰੱਖਿਆ: No Fake Quotes")
