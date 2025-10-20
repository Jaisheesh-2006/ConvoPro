from llama_index.llms.ollama import Ollama

from config.settings import Settings

settings = Settings()
OLLAMA_URL = settings.OLLAMA_URL

_current_model_name=None
_current_llm_instance=None

def get_ollama_llm(model_name: str) -> Ollama:
    global _current_model_name, _current_llm_instance
    if _current_model_name==model_name and _current_llm_instance is not None:
        return _current_llm_instance
    
    llm=Ollama(model=model_name, base_url=OLLAMA_URL)
    _current_model_name=model_name
    _current_llm_instance=llm
    return llm

