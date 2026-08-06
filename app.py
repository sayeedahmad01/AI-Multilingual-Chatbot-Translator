import streamlit as st
from openai import OpenAI


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Universal AI Assistant",
    page_icon="🤖",
    layout="centered"
)


# ============================================================
# PAGE TITLE
# ============================================================

st.title("🤖 Universal AI Assistant")
st.caption("Chat • Translate • Q&A")


# ============================================================
# OPENAI API CONFIGURATION
# ============================================================

if "OPENAI_API_KEY" not in st.secrets:
    st.error(
        "❌ OPENAI_API_KEY not found.\n\n"
        "Please add OPENAI_API_KEY to "
        ".streamlit/secrets.toml"
    )
    st.stop()


api_key = st.secrets["OPENAI_API_KEY"]


try:
    client = OpenAI(api_key=api_key)

except Exception as e:
    st.error("❌ Failed to initialize OpenAI.")
    st.exception(e)
    st.stop()


# ============================================================
# SYSTEM PROMPT
# ============================================================

SYSTEM_PROMPT = """
You are a helpful Universal AI Assistant.

Follow these rules:

1. Translation:
   - If the user asks for translation, translate accurately.
   - Use the requested target language.
   - Do not add unnecessary explanations unless requested.

2. General Questions:
   - Answer clearly and conversationally.
   - Keep explanations easy to understand.

3. Technical Questions:
   - Provide accurate explanations.
   - Give code examples when useful.

4. Application Questions:
   - Explain that this is a Streamlit-based AI assistant
     powered by OpenAI.

5. Be helpful, concise, professional, and friendly.
"""


# ============================================================
# CHAT HISTORY
# ============================================================

if "messages" not in st.session_state:

    st.session_state.messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("⚙️ Settings")

    if st.button("🗑️ Clear Chat History"):

        st.session_state.messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

        st.rerun()

    st.divider()

    st.caption("Powered by OpenAI")


# ============================================================
# DISPLAY PREVIOUS MESSAGES
# ============================================================

for message in st.session_state.messages:

    if message["role"] == "system":
        continue

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ============================================================
# CHAT INPUT
# ============================================================

prompt = st.chat_input(
    "Ask me anything, or ask me to translate..."
)


# ============================================================
# PROCESS USER MESSAGE
# ============================================================

if prompt:

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Generate response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=st.session_state.messages,
                    temperature=0.7
                )

                assistant_response = (
                    response.choices[0]
                    .message
                    .content
                )

                st.markdown(assistant_response)

                # Save response
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": assistant_response
                    }
                )

            except Exception as e:

                st.error("❌ OpenAI API Error")

                st.exception(e)git add README.md
