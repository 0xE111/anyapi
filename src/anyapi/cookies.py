import json
from http.cookiejar import CookieJar
from pathlib import Path

from requests.cookies import cookiejar_from_dict


def load_cookies(path: Path) -> CookieJar:
    """
    Load cookies from a json file of format:

    [
    {
        "domain": "one.com",
        # ...
        "value": "12345"
    },
    {
        "domain": "two.com",
        # ...
        "value": "12345"
    },
    ...
    """

    return cookiejar_from_dict({
        item['name']: item['value']
        for item in json.loads(path.read_text())
    })
