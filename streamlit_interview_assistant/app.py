import streamlit as st
import openai

st.set_page_config(page_title="AI Interview Assistant", layout="centered")
st.title("🤖 AI Interview Assistant")
st.markdown("Ask any interview question below.")

openai.api_key = st.secrets["OPENAI_API_KEY"]

question = st.text_input("Enter your question here:", "")

if st.button("Get Answer") and question:
    with st.spinner("Thinking..."):
        client = openai.OpenAI()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an AI interview assistant that gives helpful and professional answers."},
                {"role": "user", "content": question}
            ]
        )
        answer = response.choices[0].message.content
        st.markdown("### 💬 AI Answer:")
        st.success(answer)
