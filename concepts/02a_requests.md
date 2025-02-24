# Requests

Python comes with a number of ways to make HTTP requests as part of its standard library. However, a very commonly used package is [requests](https://docs.python-requests.org/en/latest/index.html).

There are two primary means of using the API that requests provide; via function calls or through a [`Session`](https://docs.python-requests.org/en/latest/user/advanced/#session-objects) object. Regardless, both ways entail working with [`Response`](https://docs.python-requests.org/en/latest/api/#requests.Response) objects to access the data returned or handle any errors raised. 

## Using function calls

```python
import requests

def get_data():
    response = requests.get("http://example.com")

    if response.status_code == 200:
        return response.text
    else:
        raise RuntimeError(f"Failed with a HTTP {response.status_code} status code.") 
```

This works, but is a bit too restrictive. There are other HTTP status codes than 200 that signal a succesful request, and requests can be redirected via HTTP 3xx responses which the `requests` package handles.

To aid us, `Response` objects have a useful method, `raise_for_status` to clean this up. Any 4xx or 5xx HTTP status code will result in an exception being raised, but otherwise `raise_for_status ` will simply return `None.`

```python
import requests

def get_data():
    response = requests.get("http://example.com")
    response.raise_for_status()
    return response.text
```

In addition to [`get`](https://docs.python-requests.org/en/latest/api/#requests.get), there are similar functions for other HTTP verbs such as [`post`](https://docs.python-requests.org/en/latest/api/#requests.post) for `POST`, [`delete`](https://docs.python-requests.org/en/latest/api/#requests.delete) for `DELETE`, [`patch`](https://docs.python-requests.org/en/latest/api/#requests.patch) for `PATCH`, and [`put`](https://docs.python-requests.org/en/latest/api/#requests.put) for `PUT`.

## Using a session object

Under the hood, the aformentioned functions actually goes through an implicit [`Session`](https://docs.python-requests.org/en/latest/user/advanced/#session-objects) object. By creating your own session, you can control and coordinate the behaviour over multiple requests.

For example, instead of setting the HTTP header that you want the response from the server to be in JSON on every single request, you can add it to your session headers. All requests going through the session object will then ask for the response as JSON. Sessions are also very useful when working with cookies.

```python
import requests

headers = {"Content-Type": "application/json"}

requests.get("https://example.com/data", headers=headers)
requests.get("https://example.com/more_data", headers=headers)
requests.get("https://example.com/even_more_data", headers=headers)
```

```python
from requests import Session

headers = {"Content-Type": "application/json"}
session = Session(headers=headers)

session.get("https://example.com/data")
session.get("https://example.com/more_data")
session.get("https://example.com/even_more_data")
```

Since it is very common to work with API:s returning JSON data, `Response` objects also has a method for parsing the response as a JSON structure. The unparsed data can still be accessed through the `text` attribute of the response object.

```python
response = requests.get("https://example.com/data")
response.raise_for_status()
return response.json()
```

## Resources

* The [requests](https://docs.python-requests.org/en/latest/index.html) documentation.
* Wikipedia's list of [HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) and their meaning.
* If you want to test your code using requests or further dig into the internals of what goes on under the hood of it, you can have a look at the package [`requtests`](https://github.com/funnel-io/requtests).

## Exercises

First see _concepts/02b_breakpoints.md_.
