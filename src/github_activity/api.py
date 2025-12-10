import requests

def getUserData(username: str) -> dict:
    URL = f"https://api.github.com/users/{username}/events"

    response = requests.get(URL)

    if not response:
        raise Exception(f"Non-success status code: {response.status_code}")

    data = response.json()

    # Tenta carregar o hook de debug local (arquivo ignorado pelo git).
    # Se o arquivo não existir (produção), o erro é ignorado silenciosamente.
    try:
        from . import _debug_hook
        _debug_hook.save_debug_data(username, data)
    except ImportError:
        pass

    return data