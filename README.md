This script is still in development, only the beta version is available!
=========================================================================
This script will help you check your proxies.
This is useful for parsing, or personal purposes.

Install
-------
-        git clone https://github.com/X-Dendi/Proxy-Get
-        cd Proxy-Get
-        chmod +x Proxy-Get.py
-        python3 Proxy-Get.py

This is how a successful connection to the service looks like
-------------------------------------------------------------
```mermaid
graph LR
A[Script] --> B(Proxy)
B --> D{Web Site}
D -x B
B -x A
```
