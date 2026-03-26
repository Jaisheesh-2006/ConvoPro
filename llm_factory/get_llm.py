from llama_index.llms.groq import Groq

from config.settings import Settings

settings = Settings()

_current_model_name = None
_current_llm_instance = None


def get_groq_llm(model_name: str) -> Groq:
    global _current_model_name, _current_llm_instance
    if _current_model_name == model_name and _current_llm_instance is not None:
        return _current_llm_instance

    llm = Groq(model=model_name, api_key=settings.GROQ_API_KEY)
    _current_model_name = model_name
    _current_llm_instance = llm
    return llm

