import requests

# Initialize a shared HTTP session with default headers
session = requests.Session()
session.headers.update({
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Mac OS X 13_0) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/115.0.5790.170 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,",
    "Accept-Language": "ru-RU,ru;q=0.9",
    "Referer": "https://www.google.com/"
})

# Base URLs for target marketplaces
BASE_URLS = {
    "wildberries": "https://www.wildberries.ru",
    "ozon": "https://www.ozon.ru",
    "yandex_market": "https://market.yandex.ru"
}
