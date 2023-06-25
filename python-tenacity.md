```
import requests
import tenacity

@tenacity.retry(
    stop=tenacity.stop_after_attempt(3),  # Retry 3 times
    wait=tenacity.wait_fixed(1),          # Wait 1 second between retries
    retry=tenacity.retry_if_exception_type(requests.exceptions.RequestException)  # Retry on RequestException
)
def get_google_homepage():
    response = requests.get('http://www.google.com')
    response.raise_for_status()  # Raise an exception if the request was not successful
    return response

try:
    result = get_google_homepage()
    print("Request succeeded:", result.status_code)
except requests.exceptions.RequestException as e:
    print("Request failed:", str(e))
```