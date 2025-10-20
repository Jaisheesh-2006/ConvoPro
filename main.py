import streamlit as st

from services.get_models_list import get_models_list
from services.get_title import get_title
from services.chat_utilities import get_answer

from db.conversations import (
    create_new_conversation,
    add_message,
    get_conversation,
    get_all_conversations
)

st.set_page_config(page_title="ConvoPro", page_icon="😎",layout="centered")
st.title("ChatGPT Clone - ConvoPro 🤷‍♂️")

# --- MODELS ---
if "OLLAMA_MODELS" not in st.session_state:
    st.session_state.OLLAMA_MODELS = get_models_list()

selected_model=st.selectbox("Select Model",st.session_state.OLLAMA_MODELS)

# ---- Session state ----
st.session_state.setdefault("conversation_id", None)
st.session_state.setdefault("conversation_title", None)
st.session_state.setdefault("chat_history", [])  # [{role, content}]

# ---- Sidebar ----

with st.sidebar:
    st.header("🔥 Chats")
    conversations=get_all_conversations()

    if st.button("➕ New Chat"):
        st.session_state.conversation_id=None
        st.session_state.conversation_title=None
        st.session_state.chat_history=[]
    for cid,title in conversations.items():
        is_selected = cid == st.session_state.conversation_id
        label=f"**{title}**" if is_selected else title
        if st.button(label,key=f"conv_{cid}"):
            st.session_state.conversation_id=cid
            conv=get_conversation(cid)
            st.session_state.chat_history=[{"role":msg["role"],"content":msg["content"]} for msg in conv.get("messages",[])]
            st.session_state.conversation_title=conv.get("title","Untitled Conversation")

# ---- Show chat so far ----
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---- New message ----
user_query=st.chat_input("Ask me anything?")
if user_query:
    # 1) Show + store user message in UI state
    st.chat_message("user").markdown(user_query)
    st.session_state.chat_history.append({"role": "user", "content": user_query})
    # 2) Create or update conversation in DB
    if st.session_state.conversation_id is None:
        # create a new conversation
        try:
            title = get_title(user_query,selected_model) or "Untitled Conversation"
        except Exception:
            print("Error occured")
            title = "Untitled Conversation"
        
        conv_id = create_new_conversation(title=title, role="user", content=user_query)
        st.session_state.conversation_title = title
        st.session_state.conversation_id = conv_id
    else:
        # add user message to existing conversation
        add_message(st.session_state.conversation_id, "user", user_query)
    
    # 3) Get assistant answer
    assistant_response = get_answer(selected_model, st.session_state.chat_history)

    # 4) Show + store assistant message in UI state
    st.chat_message("assistant").markdown(assistant_response)
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    # 5) Add assistant message to conversation in DB
    add_message(st.session_state.conversation_id, "assistant", assistant_response)
    
