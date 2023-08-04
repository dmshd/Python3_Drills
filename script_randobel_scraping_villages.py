import json
import logging

import requests

# cookies = {
#     "PHPSESSID": "b67cb71aaa1fdd51d5cbf4a9b907e37f",
#     "sticky": "0",
#     "EU_COOKIE_LAW_CONSENT": "true",
#     "Zend_Auth_RememberMe": "1",
# }

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
    "Accept": "text/plain, */*; q=0.01",
    "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
    # 'Accept-Encoding': 'gzip, deflate, br',
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive",
    "Referer": "https://www.randobel.be/track/map/lg/fr?rando%5B%5D=4&rando%5B%5D=405&distance=-1&elevation=-1&commune=&user=&balise=0&gps=0&roadbook=0&video=0&keyword=&stype=A&lg=&newsearch=1&uid=&submit=Envoyer",
    # 'Cookie': 'PHPSESSID=b67cb71aaa1fdd51d5cbf4a9b907e37f; sticky=0; EU_COOKIE_LAW_CONSENT=true; Zend_Auth_RememberMe=1',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

response = requests.get("https://www.randobel.be/village/ajaxautocomplete?term=%", headers=headers)

# Save JSON response as human readable format to file
with open("randobel_villages.json", "w") as f:
    json.dump(response.json(), f, indent=4)
