import json
from urllib import request
from urllib.error import HTTPError, URLError

from django.conf import settings


class OpenClowError(Exception):
    """Raised when OpenClow integration cannot complete a request."""


def ask_openclow(prompt: str) -> str:
    cleaned_prompt = (prompt or "").strip()
    if not cleaned_prompt:
        raise OpenClowError("Prompt is empty.")

    if not settings.OPENCLOW_API_TOKEN:
        raise OpenClowError("OpenClow token is not configured.")

    payload = {
        "model": settings.OPENCLOW_MODEL,
        "messages": [
            {"role": "user", "content": cleaned_prompt},
        ],
    }

    req = request.Request(
        settings.OPENCLOW_API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {settings.OPENCLOW_API_TOKEN}",
        },
        method="POST",
    )

    try:
        with request.urlopen(req, timeout=settings.OPENCLOW_TIMEOUT_SECONDS) as response:
            raw_response = response.read().decode("utf-8")
    except HTTPError as exc:
        error_body = exc.read().decode("utf-8", errors="ignore") if exc.fp else ""
        raise OpenClowError(f"OpenClow API HTTP error {exc.code}: {error_body}") from exc
    except URLError as exc:
        raise OpenClowError(f"OpenClow API network error: {exc.reason}") from exc

    try:
        parsed = json.loads(raw_response)
        content = parsed["choices"][0]["message"]["content"].strip()
    except (json.JSONDecodeError, KeyError, IndexError, TypeError) as exc:
        raise OpenClowError("OpenClow API returned an unexpected response format.") from exc

    if not content:
        raise OpenClowError("OpenClow API returned an empty answer.")

    return content
