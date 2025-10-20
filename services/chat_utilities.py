from llama_index.core.llms import ChatMessage, MessageRole
from llm_factory.get_llm import get_ollama_llm

def get_answer(model_name:str,chat_history):
    llm=get_ollama_llm(model_name)
    
    # prepend a system message to set the behavior of the assistant
    messages=[ChatMessage(role=MessageRole.SYSTEM, content="You are a helpful assistant that provides accurate and concise information based on the user's queries.")]

    # add the chat history messages
    messages.extend(
        ChatMessage(role=MessageRole[msg['role'].upper()], content=msg['content']) for msg in chat_history
    )

    respone=llm.chat(messages=messages)
    return respone.message.content