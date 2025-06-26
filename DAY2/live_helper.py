#live_helper.py

import requests

def translate_libre(text, source="en", target="ko"):
    url = "https://api.mymemory.translated.net/get"
    params = {
        "q": text,
        "langpair": f"{source}|{target}"
    }
    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data['responseData']['translatedText']
    except Exception as e:
        return f"번역 실패: {e}"
