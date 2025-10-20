from config.settings import Settings

settings=Settings()


def get_models_list() -> list:
    model_list=[model.strip() for model in settings.OLLAMA_MODELS.split(",") if model.strip()]
    return model_list