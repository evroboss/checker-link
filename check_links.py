import urllib.parse

import requests


def check_url(url):
    parsed_url = urllib.parse.urlparse(url)
    if not all([parsed_url.scheme, parsed_url.netloc]):
        return f"Некорректный URL: {url} (нет схемы и домена)"
    try:
        response = requests.get(url, timeout=5)
        status_code = response.status_code
        if status_code == 200:
            return f"OK: {url} — работает"
        else:
            return f"Ошибка {status_code}: {url} — не доступен"
    except requests.exceptions.RequestException as e:
        return f"Ошибка: {url} — не доступен (исключение: {e})"


urls = [
    "https://example.com",
    "https://nonexistent-domain-12345.com",
    "https://python.org",
    "not-a-valid-url"
]

for url in urls:
    print(check_url(url))
