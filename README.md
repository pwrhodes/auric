# auric

Python module to assist with managing URLs in your Python code. Instead of simply storing your URLs as strings, making them hard to interogate and update, wouldn't you prefer to store them in a mutable instance? With support for protocols, domains, paths, query strings and more, this will improve your experience when writing code involving URLs.

## How to use

Here is an example:

```python
import requests

from auric import URL

my_url = URL(hostname="www.google.com", path="search")
if "secure":
    my_url.protocol = "https"
my_url.query = "q=testing"
requests.get(my_url.as_string())
```
