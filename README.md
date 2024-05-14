# <p align="center">aCryptoPayAPI</p>
Simple Python implementation of [Crypto Pay API](https://help.crypt.bot/crypto-pay-api) (Crypto Pay is a payment system based on [@CryptoBot](http://t.me/CryptoBot)), but asynchronic, and a little more features! 
# Installation
Install from sources
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
