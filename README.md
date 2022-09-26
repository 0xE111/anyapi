# AnyAPI

AnyAPI is a small library to get rid of boilerplate code reused in many projects where interaction with APIs is needed.

AnyAPI:
* uses `requests.Session`
* has default timeout
* has configurable pool size
* has retry policy in case of 429 error
* has `get` and `post` methods defined

## How to use

```sh
pip install anyapi2
```

```python
from anyapi import API


class SomeServiceAPI(API):
    BASE_URL = 'https://some-api-service.com'


some_service = SomeServiceAPI()
response = some_service.get('/v1/items')
response.raise_for_status()
result = response.json()
```
