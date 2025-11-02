import requests
from tqdm import tqdm

def get_request(url: str, params: dict | None = None, headers: dict | None = None, timeout: int = 15) -> dict:
    try:
        tqdm.write(f"[GET] URL : {url}")
        resp = requests.get(url, params=params, headers=headers or {}, timeout=timeout)
        resp.raise_for_status()
        if "application/json" in resp.headers.get("Content-Type", ""):
            return resp.json()
        return {}
    except Exception as error:
        tqdm.write(f"Exception Occurred. {error}")
        return {}