[![PyPi Package Version](https://img.shields.io/pypi/v/aCryptoPayAPI.svg)](https://pypi.python.org/pypi/aCryptoPayAPI)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/aCryptoPayAPI.svg)](https://pypi.python.org/pypi/aCryptoPayAPI)
[![PyPi downloads](https://img.shields.io/pypi/dm/aCryptoPayAPI.svg)](https://pypi.org/project/aCryptoPayAPI/)

# <p align="center">aCryptoPayAPI</p>
Simple Python implementation of [Crypto Pay API](https://help.crypt.bot/crypto-pay-api) (Crypto Pay is a payment system based on [@CryptoBot](http://t.me/CryptoBot)), but asynchronic, and a little more features! 
# Installation
Installation using pip (a Python package manager):
```
$ pip install aCryptoPayAPI
```

# Usage
Everything is as simple as the [API](https://help.crypt.bot/crypto-pay-api#available-methods) itself.
1. Create pyCryptoPayAPI instance
2. Access API methods in pythonic notation (getInvoices -> get_invoices)
```
from aCryptoPayAPI import aCryptoPayAPI
client = aCryptoPayAPI(api_token="zzz")
print(client.get_balance())
```
You can also check tests.py.

# Exceptions
Exceptions are rised using pyCryptoPayException class.
